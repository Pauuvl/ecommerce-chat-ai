# Ecommerce Chat AI

API desarrollada con FastAPI siguiendo arquitectura limpia (Clean Architecture), que permite gestionar productos y realizar consultas mediante inteligencia artificial.

## Tecnologías

- FastAPI
- SQLAlchemy
- SQLite
- Docker
- Google Generative AI (Gemini)

## Ejecución del proyecto

### Local

pip install -r requirements.txt  
python -m uvicorn src.infrastructure.api.main:app --reload  

### Docker

docker-compose up --build  

## Endpoints

### GET /products
Obtiene la lista de productos disponibles.

### POST /chat
Permite interactuar con la IA.

Ejemplo:

{
  "session_id": "123",
  "message": "Recomiendame productos"
}

## Base de datos

- SQLite
- Ubicación: data/ecommerce_chat.db

## Evidencias

Las capturas se encuentran en la carpeta `evidencias/`.

## Autor

Paulina Velasquez Londoño