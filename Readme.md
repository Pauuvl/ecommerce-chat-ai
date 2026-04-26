Perfecto, aquí tienes el **README en formato código listo para copiar completo** 👇

````markdown
#  E-commerce Chat API con IA (Clean Architecture)

API desarrollada con FastAPI que permite gestionar productos de un e-commerce e interactuar con un asistente inteligente basado en IA (Google Gemini), siguiendo el patrón de Clean Architecture.

---

## Tecnologías utilizadas

- Python 3.10+
- FastAPI  
- SQLAlchemy  
- SQLite  
- Docker  
- Google Gemini AI  
- Pydantic  

---

##  Arquitectura

El proyecto sigue **Clean Architecture**, dividido en 3 capas:

###  1. Dominio (`src/domain`)
Contiene las reglas de negocio puras:
- Entidades (`Product`, `ChatMessage`, `ChatContext`)
- Interfaces de repositorios  

---

###  2. Aplicación (`src/application`)
Contiene la lógica de negocio:
- Servicios (`ProductService`, `ChatService`)
- DTOs (validación de datos)  

---

###  3. Infraestructura (`src/infrastructure`)
Contiene implementaciones concretas:
- Base de datos (SQLite)  
- Repositorios  
- API (FastAPI)  
- Integración con IA (Gemini)  

---

## Instalación y ejecución

### 🔹 1. Clonar repositorio

```bash
git clone <TU_REPOSITORIO>
cd ecommerce-chat-ai
````

---

###  2. Crear entorno virtual

```bash
python -m venv venv
```

Activar en Windows:

```bash
venv\Scripts\activate
```

---

###  3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

###  4. Configurar variables de entorno

Crear archivo `.env`:

```
GEMINI_API_KEY=tu_api_key_aqui
```

---

###  5. Ejecutar la aplicación

```bash
python -m uvicorn src.infrastructure.api.main:app --reload
```

---

###  6. Acceder a Swagger

[http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Docker

Ejecutar con Docker:

```bash
docker-compose up --build
```

---

##  Endpoints disponibles

###  Health Check

```
GET /health
```

---

###  Productos

Obtener todos los productos:

```
GET /products
```

Obtener producto por ID:

```
GET /products/{id}
```

---

###  Chat con IA

Enviar mensaje:

```
POST /chat
```

Body:

```json
{
  "session_id": "123",
  "message": "Recomiéndame productos"
}
```

---

Obtener historial:

```
GET /chat/history/{session_id}
```

---

Eliminar historial:

```
DELETE /chat/history/{session_id}
```

---

##  Funcionalidades principales

 Gestión de productos
 Chat inteligente con IA
 Memoria conversacional por sesión
 Arquitectura limpia (Clean Architecture)
 Persistencia con SQLite
 Contenerización con Docker

---

## Testing

Ejecutar pruebas:

```bash
pytest
```

---

## Evidencias

Las evidencias se encuentran en la carpeta:

```
/evidencias
```

Incluyen:

Swagger UI
Logs de Docker
Contenedores corriendo
Llamados a la API
Base de datos

---

##  Autor

Paulina Velásquez

---

##  Notas

 El proyecto utiliza Google Gemini como modelo de IA
 Se requiere conexión a internet para el funcionamiento del chat
 Base de datos SQLite local

