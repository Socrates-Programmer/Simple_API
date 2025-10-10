Simple API

Base mínima de una API en Flask con estructura modular, JWT, migraciones de base de datos y soporte para Docker. Ideal para proyectos educativos y prototipos rápidos.

✨ Características

Flask organizado por módulos (models/, resources/, etc.)

SQLAlchemy + Flask-Migrate para versionar el esquema

JWT con blocklist para invalidar tokens (logout/rotación)

Marshmallow (o esquemas en schema.py) para validación/serialización

Dockerfile para empaquetado y despliegue reproducible

Soporte para variables de entorno vía .flaskenv/.env

📁 Estructura del proyecto
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

🧰 Requisitos

Python 3.10+

pip y (opcional) venv

(Opcional) Docker 24+ / Docker Desktop

Motor de BD:

Desarrollo: SQLite (sqlite:///data.db)

Producción: PostgreSQL o MySQL

⚙️ Configuración (local)

Clonar e instalar dependencias

git clone https://github.com/Socrates-Programmer/Simple_API.git
cd Simple_API
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt


Variables de entorno
Crea un .flaskenv (para desarrollo) o exporta variables en tu shell:

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


Migraciones de BD

flask db upgrade


Ejecutar

flask run
# http://localhost:5000

🐳 Ejecutar con Docker

Build & run (usando dockerfile del repo):

docker build -t simple-api .
docker run --name simple-api \
  --env-file .flaskenv \
  -p 5000:5000 simple-api


(Opcional) si agregas docker-compose.yml, podrías usar:

docker compose up --build

🔑 Autenticación (JWT)

Login: emite un access_token (y opcionalmente refresh_token).

Logout: agrega el token a blocklist para invalidarlo.

En producción, guarda JWT_SECRET_KEY fuera del repo (secret manager/vars del entorno).

🔌 Endpoints (plantilla)

Actualiza los paths/nombres según tus blueprints reales.

GET / — Health/Hello (estado rápido del servicio)

POST /auth/login — recibe credenciales, responde con JWT

DELETE /auth/logout — invalida token activo (blocklist)

GET /items — lista de recursos

POST /items — crea recurso

GET /items/<id> — detalle

PUT /items/<id> — actualización

DELETE /items/<id> — borrado

Ejemplos curl
# Health
curl -i http://localhost:5000/

# Login (ejemplo)
curl -s -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","password":"demo"}'

# Con token
TOKEN="<pega-tu-access-token>"
curl -s http://localhost:5000/items \
  -H "Authorization: Bearer $TOKEN"

🧪 Pruebas (sugerencia)

Estructura sugerida:

tests/
  ├─ conftest.py
  ├─ test_health.py
  └─ test_items.py


Ejecutar:

pytest -q

♻️ Comandos de migración
flask db init           # solo una vez (si no existe migrations/)
flask db migrate -m "mensaje"
flask db upgrade
flask db downgrade

🔒 Buenas prácticas

No subir .flaskenv/.env con secretos

Rotar JWT_SECRET_KEY periódicamente

Forzar TLS en producción (Nginx/Reverse Proxy)

Usar cuentas de BD con privilegios mínimos

🚀 Despliegue (hint)

Gunicorn + Nginx detrás de un proxy inverso

Docker en VPS/Cloud (Lightsail, EC2, GCE, etc.)

DATABASE_URL apuntando a un servicio gestionado (p. ej., RDS)
