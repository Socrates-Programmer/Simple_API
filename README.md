# Simple API

> **Base modular en Flask 🐍**

Una base mínima y robusta para construir una API RESTful con Flask. Incluye:
- Estructura modular
- Seguridad JWT
- Gestión de bases de datos con migraciones
- Soporte completo para Docker

Ideal para proyectos educativos, prototipos rápidos y empezar con las mejores prácticas de Flask.

---

## ✨ Características Principales

- **Estructura Modular:**  
  Flask organizado por blueprints y módulos (`models/`, `resources/`, etc.).

- **Base de Datos:**  
  SQLAlchemy + Flask-Migrate para esquema versionado y fácil de actualizar.

- **Autenticación Segura:**  
  JWT con Blocklist para invalidar tokens (logout/rotación).

- **Validación de Datos:**  
  Marshmallow (o esquemas en `schema.py`) para serialización/validación limpia.

- **Despliegue Simple:**  
  Incluye Dockerfile para empaquetado y despliegue reproducible.

- **Configuración:**  
  Soporte para `.flaskenv` (desarrollo) y variables estándar (producción).

---

## 📁 Estructura del Proyecto

```
Simple_API/
├─ app.py
├─ db.py
├─ blocklist.py
├─ schema.py
├─ requirements.txt
├─ dockerfile
├─ .flaskenv                      # 🔒 Variables locales (no subir secretos)
├─ models/                        # Modelos SQLAlchemy
├─ resources/                     # Blueprints/Endpoints de la API
├─ migrations/                    # Historial de Alembic/Migrate
└─ docker/                        # Assets de despliegue (si aplica)
```

---

## 🧰 Requisitos

- Python 3.10+
- pip y venv (opcional)
- Docker 24+ / Docker Desktop (opcional)

**Motor de BD:**  
- Desarrollo: SQLite (`sqlite:///data.db`)  
- Producción: Recomendado PostgreSQL o MySQL

---

## ⚙️ Configuración (Local)

### 1. Clonar e Instalar Dependencias

```bash
git clone https://github.com/Socrates-Programmer/Simple_API.git
cd Simple_API
```

**Crear y activar entorno virtual:**

```bash
python -m venv .venv
```

- **Windows (CMD/PowerShell):** `.venv\Scripts\activate`
- **Linux/Mac:**  
  ```bash
  source .venv/bin/activate
  ```

**Instalar dependencias:**

```bash
pip install -r requirements.txt
```

---

### 2. Variables de Entorno

Crea un archivo `.flaskenv` en la raíz (solo para desarrollo local):

```
FLASK_APP=app.py
FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000

# Seguridad: ¡Cambia este valor!
JWT_SECRET_KEY=cambia-esto-por-un-secreto-seguro

# Base de datos
# Desarrollo (SQLite)
DATABASE_URL=sqlite:///data.db

# Producción (Postgres, ejemplo)
# DATABASE_URL=postgresql+psycopg2://user:pass@host:5432/dbname
```

---

### 3. Migraciones de Base de Datos

Aplica el esquema inicial a tu base de datos:

```bash
flask db upgrade
```

---

### 4. Ejecutar

```bash
flask run
```

**API corriendo en:**  
http://localhost:5000

---

## 🐳 Ejecutar con Docker

Construye la imagen y ejecuta el contenedor, usando las variables de entorno desde `.flaskenv`:

```bash
docker build -t simple-api .
docker run --name simple-api \
  --env-file .flaskenv \
  -p 5000:5000 simple-api
```

**(Opcional)** Si agregas `docker-compose.yml`:

```bash
docker compose up --build
```

---

## 🔑 Autenticación (JWT)

| Endpoint         | Descripción                                      |
|------------------|--------------------------------------------------|
| POST /auth/login | Recibe credenciales y emite un access_token.     |
| DELETE /auth/logout | Invalida el token activo agregándolo a blocklist. |

> ⚠️ **Práctica de Seguridad:**  
> En producción, la variable `JWT_SECRET_KEY` debe gestionarse con un Secret Manager y no estar en archivos como `.flaskenv` ni en el repositorio.

---

## 🔌 Endpoints (Plantilla)

🔐 Autenticación y Usuarios

| Método | Endpoint              | Descripción                                     | Seguridad   |
| ------ | --------------------- | ----------------------------------------------- | ----------- |
| POST   | `/register`           | Registro de nuevo usuario                       | Pública     |
| POST   | `/login`              | Inicia sesión y devuelve access & refresh token | Pública     |
| POST   | `/refresh`            | Renueva el access token usando refresh token    | JWT Refresh |
| POST   | `/logout`             | Cierra sesión (token se agrega a blocklist)     | JWT         |
| GET    | `/user/<int:user_id>` | Obtiene un usuario por ID                       | Pública     |
| DELETE | `/user/<int:user_id>` | Elimina un usuario por ID                       | Pública     |

📦 Items

| Método | Endpoint              | Descripción                       | Seguridad   |
| ------ | --------------------- | --------------------------------- | ----------- |
| GET    | `/item`               | Lista todos los items             | JWT         |
| POST   | `/item`               | Crea un nuevo item                | JWT (Fresh) |
| GET    | `/item/<int:item_id>` | Obtiene un item por ID            | JWT         |
| PUT    | `/item/<int:item_id>` | Actualiza o crea un item (upsert) | Pública     |
| DELETE | `/item/<int:item_id>` | Elimina un item                   | JWT         |

🏬 Stores

| Método | Endpoint                | Descripción               | Seguridad |
| ------ | ----------------------- | ------------------------- | --------- |
| GET    | `/store`                | Lista todas las tiendas   | Pública   |
| POST   | `/store`                | Crea una nueva tienda     | Pública   |
| GET    | `/store/<int:store_id>` | Obtiene una tienda por ID | Pública   |
| DELETE | `/store/<int:store_id>` | Elimina una tienda        | Pública   |

🏷️ Tags

| Método | Endpoint                               | Descripción                                | Seguridad |
| ------ | -------------------------------------- | ------------------------------------------ | --------- |
| GET    | `/store/<int:store_id>/tag`            | Lista los tags de una tienda               | Pública   |
| POST   | `/store/<int:store_id>/tag`            | Crea un tag en una tienda                  | Pública   |
| GET    | `/tag/<int:tag_id>`                    | Obtiene un tag por ID                      | Pública   |
| DELETE | `/tag/<int:tag_id>`                    | Elimina un tag si no está asociado a items | Pública   |
| POST   | `/item/<int:item_id>/tag/<int:tag_id>` | Asocia un tag a un item                    | Pública   |
| DELETE | `/item/<int:item_id>/tag/<int:tag_id>` | Quita un tag de un item                    | Pública   |

---

## ♻️ Comandos de Migración (Alembic)

| Comando                       | Descripción                                    |
|-------------------------------|------------------------------------------------|
| flask db init                 | Inicializa el repo de migraciones (solo 1 vez) |
| flask db migrate -m "mensaje" | Crea nuevo archivo de migración                |
| flask db upgrade              | Aplica todas las migraciones pendientes        |
| flask db downgrade            | Deshace la última migración aplicada           |

🛡️ Seguridad

Autenticación basada en JWT

Soporte para Access Token y Refresh Token

Logout implementado mediante BLOCKLIST

Algunos endpoints requieren token fresh para mayor seguridad
---

## 📫 Contacto

¿Dudas o propuestas de mejora?  
Por favor, abre un Issue en GitHub.

Email: marcosavila3005@gmail.com
