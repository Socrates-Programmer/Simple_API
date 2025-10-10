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

Ajusta estos paths según los blueprints que implementes.

| Método  | Path            | Descripción                      | Seguridad  |
|---------|-----------------|----------------------------------|------------|
| GET     | /               | Health/Hello (estado del servicio)| Pública    |
| POST    | /auth/login     | Inicia sesión y obtiene JWT       | Pública    |
| DELETE  | /auth/logout    | Cierra sesión (invalida JWT)      | Protegida  |
| GET     | /items          | Lista de recursos                 | Protegida  |
| POST    | /items          | Crea un nuevo recurso             | Protegida  |
| GET     | /items/<id>     | Detalle de recurso                | Protegida  |
| PUT     | /items/<id>     | Actualización de recurso          | Protegida  |
| DELETE  | /items/<id>     | Borrado de recurso                | Protegida  |

---

## ♻️ Comandos de Migración (Alembic)

| Comando                       | Descripción                                    |
|-------------------------------|------------------------------------------------|
| flask db init                 | Inicializa el repo de migraciones (solo 1 vez) |
| flask db migrate -m "mensaje" | Crea nuevo archivo de migración                |
| flask db upgrade              | Aplica todas las migraciones pendientes        |
| flask db downgrade            | Deshace la última migración aplicada           |

---

## 📫 Contacto

¿Dudas o propuestas de mejora?  
Por favor, abre un Issue en GitHub.

Email: marcosavila3005@gmail.com
