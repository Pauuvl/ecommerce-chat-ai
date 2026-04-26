from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.db.database import get_db, engine, Base
from src.application.product_service import ProductService
from src.application.chat_service import ChatService
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.repositories.chat_repository import ChatRepository
from src.infrastructure.db.models import ProductModel

# ==============================
# CREACIÓN DE LA APP
# ==============================
app = FastAPI(
    title="Ecommerce Chat API",
    description="API con IA para recomendación de productos",
    version="1.0.0"
)

# ==============================
# CONFIGURACIÓN CORS
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# EVENTO DE INICIO
# ==============================
@app.on_event("startup")
def startup():
    """
    Se ejecuta al iniciar la aplicación.
    - Crea las tablas
    - Inserta productos iniciales si no existen
    """
    Base.metadata.create_all(bind=engine)

    db = Session(bind=engine)

    # Si no hay productos, insertar datos iniciales
    if not db.query(ProductModel).first():
        productos = [
            ProductModel(name="Nike Air", description="Zapatillas deportivas", brand="Nike", category="Running", size="42", color="Negro", price=120, stock=5),
            ProductModel(name="Adidas Run", description="Zapatillas cómodas", brand="Adidas", category="Running", size="41", color="Blanco", price=100, stock=8),
            ProductModel(name="Puma Street", description="Zapatillas urbanas", brand="Puma", category="Casual", size="40", color="Rojo", price=90, stock=10),
            ProductModel(name="Reebok Classic", description="Estilo clásico", brand="Reebok", category="Casual", size="39", color="Blanco", price=95, stock=6),
        ]

        for p in productos:
            db.add(p)

        db.commit()
        print("✔ Productos iniciales insertados")


# ==============================
# ENDPOINTS
# ==============================

@app.get("/")
def home():
    """
    Endpoint de prueba.
    """
    return {"message": "API funcionando correctamente 🚀"}


@app.get("/health")
def health():
    """
    Verifica el estado de la API.
    """
    return {"status": "ok"}


@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    """
    Obtiene todos los productos.

    Args:
        db (Session): conexión a la base de datos

    Returns:
        list: productos disponibles
    """
    try:
        repo = ProductRepository(db)
        service = ProductService(repo)
        return service.get_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un producto por ID.
    """
    try:
        repo = ProductRepository(db)
        service = ProductService(repo)

        product = service.get_product_by_id(product_id)

        if not product:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat")
def chat(request: dict, db: Session = Depends(get_db)):
    """
    Endpoint de chat con IA.

    Body esperado:
    {
        "session_id": "123",
        "message": "Recomiéndame productos"
    }
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


@app.get("/chat/history/{session_id}")
def get_chat_history(session_id: str, db: Session = Depends(get_db)):
    """
    Obtiene el historial del chat.
    """
    try:
        repo = ChatRepository(db)
        return repo.get_session_history(session_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/chat/history/{session_id}")
def delete_chat_history(session_id: str, db: Session = Depends(get_db)):
    """
    Elimina el historial del chat.
    """
    try:
        repo = ChatRepository(db)
        repo.delete_session_history(session_id)
        return {"message": "Historial eliminado"}
    except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))