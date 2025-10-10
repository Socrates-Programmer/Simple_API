# Simple API: Base Modular en Flask 🐍

Base mínima de una API en **Flask** con estructura modular, **JWT** (JSON Web Tokens), migraciones de base de datos y soporte para **Docker**. Ideal para proyectos educativos y prototipos rápidos.

---

## ✨ Características Principales

* **Flask** organizado por módulos (`models/`, `resources/`, etc.)
* **SQLAlchemy** + **Flask-Migrate** para versionar el esquema de la base de datos.
* **JWT** con *blocklist* para invalidar tokens (logout/rotación).
* **Marshmallow** (o esquemas en `schema.py`) para validación y serialización de datos.
* **Dockerfile** para empaquetado y despliegue reproducible.
* Soporte para **variables de entorno** vía `.flaskenv`/`.env`.

---

## 📁 Estructura del Proyecto

```bash
Simple_API/
├─ app.py
├─ db.py
├─ blocklist.py
├─ schema.py
├─ requirements.txt
├─ dockerfile
├─ .flaskenv                      # variables locales (no subir secretos)
├─ models/                        # modelos SQLAlchemy
├─ resources/                     # blueprints/endpoints
├─ migrations/                    # historial de migraciones
└─ docker/                        # assets de despliegue (si aplica)
```

---

## 🧰 Requisitos

* **Python 3.10+**
* `pip` y (opcional) `venv`
* (Opcional) **Docker 24+** / Docker Desktop
* **Motor de BD:**
    * Por defecto: Puede usar **SQLite** (`sqlite:///data.db`)
    * Para producción: Recomendado **PostgreSQL** o **MySQL**

---

## ⚙️ Configuración (Local)

### 1. Clonar e instalar dependencias

```bash
git clone [https://github.com/Socrates-Programmer/Simple_API.git](https://github.com/Socrates-Programmer/Simple_API.git)
cd Simple_API
python -m venv .venv

# Windows
# .venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
2. Variables de entorno
Crea un archivo .flaskenv (para desarrollo) o exporta variables en tu shell:

```

# .flaskenv (solo dev; no subir secretos)
FLASK_APP=app.py
FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000

# Seguridad
JWT_SECRET_KEY=cambia-esto-por-un-secreto-seguro

# Base de datos
# Opción SQLite (desarrollo)
DATABASE_URL=sqlite:///data.db

# Opción Postgres (producción)
# DATABASE_URL=postgresql+psycopg2://user:pass@host:5432/dbname
3. Migraciones de BD
Aplica las migraciones iniciales a la base de datos:

```bash

flask db upgrade
4. Ejecutar

```bash

flask run
# Accede a: http://localhost:5000
🐳 Ejecutar con Docker
Build & Run
Usa el dockerfile incluido para construir y ejecutar la imagen:

```Bash

docker build -t simple-api .

docker run --name simple-api \
  --env-file .flaskenv \
  -p 5000:5000 simple-api
(Opcional) si agregas docker-compose.yml, podrías usar:

```Bash

docker compose up --build
🔑 Autenticación (JWT)
Login: emite un access_token (y opcionalmente refresh_token).

Logout: agrega el token a la blocklist para invalidarlo inmediatamente.

⚠️ En producción: Guarda JWT_SECRET_KEY fuera del repositorio (secret manager/variables del entorno).

🔌 Endpoints (Plantilla)
Actualiza los paths/nombres según tus blueprints reales.

Método	Path	Descripción
GET	/	Health/Hello (estado rápido del servicio)
POST	/auth/login	Recibe credenciales, responde con JWT
DELETE	/auth/logout	Invalida token activo (blocklist)
GET	/items	Lista de recursos
POST	/items	Crea recurso
GET	/items/<id>	Detalle de recurso
PUT	/items/<id>	Actualización de recurso
DELETE	/items/<id>	Borrado de recurso

Exportar a Hojas de cálculo
Ejemplos curl
```

# Health
curl -i http://localhost:5000/

# Login (ejemplo)
curl -s -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","password":"demo"}'

# Uso de token (ejemplo de endpoint protegido)
TOKEN="<pega-tu-access-token>"
curl -s http://localhost:5000/items \
  -H "Authorization: Bearer $TOKEN"
🧪 Pruebas (Sugerencia)
Estructura sugerida
tests/
  ├─ conftest.py
  ├─ test_health.py
  └─ test_items.py
  
Ejecutar
```Bash

pytest -q
♻️ Comandos de Migración
```Bash

flask db init           # solo una vez (si no existe migrations/)
flask db migrate -m "mensaje"
flask db upgrade
flask db downgrade
```
🔒 Buenas Prácticas
No subir .flaskenv/.env con secretos al repositorio.

Rotar JWT_SECRET_KEY periódicamente.

Forzar TLS en producción (Nginx/Reverse Proxy).

Usar cuentas de BD con privilegios mínimos.

🚀 Despliegue (Hint)
Usar Gunicorn + Nginx detrás de un proxy inverso.

Desplegar con Docker en VPS/Cloud (Lightsail, EC2, GCE, etc.).

DATABASE_URL debe apuntar a un servicio gestionado (p. ej., RDS).

🗺️ Roadmap Sugerido
Documentación OpenAPI/Swagger

CI con GitHub Actions (lint + tests)

docker-compose.yml con Postgres y pgAdmin

Ejemplos CRUD completos con validación y tests

Rate limiting / CORS configurable

🤝 Contribuir
¡Las contribuciones son bienvenidas! Sigue estos pasos:

Crea un branch: git checkout -b feature/tu-feature

Commit: git commit -m "feat: agrega X"

Push: git push origin feature/tu-feature

Abre un Pull Request


📫 Contacto
Abre un Issue con tu duda o propuesta de mejora.

--marcosavila3005@gmail.com
