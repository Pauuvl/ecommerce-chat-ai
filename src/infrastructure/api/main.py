from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.db.database import get_db, engine, Base
from src.application.product_service import ProductService
from src.application.chat_service import ChatService
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.repositories.chat_repository import ChatRepository

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    """
    Evento que se ejecuta al iniciar la aplicación.
    Se encarga de crear las tablas en la base de datos si no existen.
    """
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    """
    Endpoint de prueba para verificar que la API está funcionando.

    Returns:
        dict: mensaje de estado
    """
    return {"message": "API funcionando"}


@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    """
    Endpoint que obtiene todos los productos disponibles.

    Args:
        db (Session): sesión de base de datos

    Returns:
        list: lista de productos
    """
    try:
        repo = ProductRepository(db)
        service = ProductService(repo)
        return service.get_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat")
def chat(request: dict, db: Session = Depends(get_db)):
    """
    Endpoint para interactuar con la IA.

    Args:
        request (dict): contiene session_id y message
        db (Session): sesión de base de datos

    Returns:
        dict: respuesta de la IA
    """
    try:
        repo = ChatRepository(db)
        service = ChatService(repo)

        response = service.send_message(
            request["session_id"],
            request["message"]
        )

        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/init")
def init_data(db: Session = Depends(get_db)):
    """
    Inserta productos de prueba en la base de datos.

    Args:
        db (Session): sesión de base de datos

    Returns:
        dict: mensaje de confirmación
    """
    from src.infrastructure.db.models import ProductModel

    products = [
        ProductModel(name="Nike Air", description="Zapatillas deportivas", brand="Nike", category="Running", price=120, stock=5),
        ProductModel(name="Adidas Run", description="Zapatillas cómodas", brand="Adidas", category="Running", price=100, stock=8),
    ]

    for p in products:
        db.add(p)

    db.commit()

    return {"message": "Productos insertados"}