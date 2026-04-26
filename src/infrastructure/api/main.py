from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.db.database import get_db, engine, Base
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.repositories.chat_repository import ChatRepository
from src.application.product_service import ProductService
from src.application.chat_service import ChatService
from src.infrastructure.db.models import ProductModel

# Crear app
app = FastAPI()

# CORS (importante para frontend / pruebas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------- STARTUP ----------
@app.on_event("startup")
def startup():
    """
    Crea las tablas automáticamente al iniciar la app
    """
    Base.metadata.create_all(bind=engine)


# ---------- HEALTH ----------
@app.get("/health")
def health():
    """
    Endpoint para verificar que la API está viva (tests)
    """
    return {"status": "ok"}


# ---------- HOME ----------
@app.get("/")
def home():
    return {"message": "API funcionando"}


# ---------- PRODUCTS ----------
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    try:
        repo = ProductRepository(db)
        service = ProductService(repo)
        return service.get_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    try:
        repo = ProductRepository(db)
        service = ProductService(repo)
        return service.get_product_by_id(product_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# ---------- CHAT ----------
@app.post("/chat")
def chat(request: dict, db: Session = Depends(get_db)):
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
def get_history(session_id: str, db: Session = Depends(get_db)):
    try:
        repo = ChatRepository(db)
        service = ChatService(repo)
        return service.get_history(session_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/chat/history/{session_id}")
def delete_history(session_id: str, db: Session = Depends(get_db)):
    try:
        repo = ChatRepository(db)
        service = ChatService(repo)
        service.delete_history(session_id)
        return {"message": "Historial eliminado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------- INIT DATA ----------
@app.get("/init")
def init_data(db: Session = Depends(get_db)):
    """
    Inserta datos de prueba en la base de datos
    """
    try:
        products = [
            ProductModel(
                name="Nike Air",
                description="Zapatillas deportivas",
                brand="Nike",
                category="Running",
                price=120,
                stock=5
            ),
            ProductModel(
                name="Adidas Run",
                description="Zapatillas cómodas",
                brand="Adidas",
                category="Running",
                price=100,
                stock=8
            ),
            ProductModel(
                name="Puma Street",
                description="Zapatillas urbanas",
                brand="Puma",
                category="Casual",
                price=90,
                stock=10
            ),
        ]

        for p in products:
            db.add(p)

        db.commit()

        return {"message": "Productos insertados"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))