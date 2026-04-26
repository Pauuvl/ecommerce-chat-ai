
#  Ecommerce Chat API

API REST desarrollada con FastAPI que permite gestionar productos y un sistema de chat inteligente usando IA.

---

##  Descripción

Este proyecto implementa una arquitectura en capas (Domain, Application, Infrastructure) para un sistema de ecommerce con funcionalidades de:

- Gestión de productos
- Chat inteligente con historial por sesión
- Persistencia en base de datos SQLite
- Contenerización con Docker
- Testing automatizado con Pytest

---

## Arquitectura

El proyecto sigue una arquitectura limpia dividida en:

```

src/
│
├── domain/                # Entidades y lógica de negocio pura
├── application/           # Casos de uso (servicios)
├── infrastructure/        # DB, API, repositorios, IA
│   ├── api/
│   ├── db/
│   ├── repositories/
│   └── llm_providers/


````

---

##  Tecnologías utilizadas

- FastAPI
- SQLAlchemy
- SQLite
- Docker
- Pytest
- Gemini (IA simulada en testing)

---
````
##  Ejecución local

### 1. Crear entorno virtual

```bash
python -m venv venv
````

### 2. Activar entorno

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar servidor

```bash
uvicorn src.infrastructure.api.main:app --reload
```

---

## Docker

### Construir contenedor

```bash
docker-compose build
```

### Ejecutar

```bash
docker-compose up
```

---

## Endpoints

###  Home

```
GET /
```

Respuesta:

```json
{
  "message": "API funcionando"
}
```

---

### Health Check

```
GET /health
```

---

###  Obtener productos

```
GET /products
```

---

###  Obtener producto por ID

```
GET /products/{id}
```

---

###  Inicializar datos

```
GET /init
```

---

###  Chat con IA

```
POST /chat
```

Body:

```json
{
  "session_id": "123",
  "message": "Hola"
}
```

---

###  Historial de chat

```
GET /chat/history/{session_id}
```

---

###  Eliminar historial

```
DELETE /chat/history/{session_id}
```

---

##  Funcionamiento del Chat

* Guarda cada mensaje en la base de datos
* Recupera historial reciente
* Genera contexto
* Llama al proveedor de IA
* Guarda la respuesta

 En modo testing, la IA es simulada.

---

##  Testing

### Ejecutar pruebas

```bash
pytest -v
```

### Tests incluidos

* API:

  * Home
  * Health

* Productos:

  * Obtener todos
  * Obtener por ID

* Chat:

  * Envío de mensaje
  * Historial
  * Eliminación

---

## Variables de entorno

Crear archivo `.env`:

```
TESTING=0
```

En testing:

```
TESTING=1
```

---

##  Base de datos

Ubicación:

```
data/ecommerce_chat.db
```

Tablas:

* products
* chat_memory

---

##  Modelo de datos

### Producto

* id
* name
* description
* brand
* category
* size
* color
* price
* stock

---

### ChatMemory

* id
* session_id
* role
* message
* timestamp

---


## Problemas comunes

###  Error 500 en /chat

Solución:

* Verificar variable TESTING=1 en pruebas
* Confirmar que GeminiProvider no llama API real

---

###  No module named 'src'

Solución:

```bash
set PYTHONPATH=.
```

---

###  Base de datos vacía

Ejecutar:

```
GET /init
```

---


## 👩‍💻 Autor

Paulina Velásquez



