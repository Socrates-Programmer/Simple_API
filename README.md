Simple API: Base Modular en Flask 🐍

Base mínima de una API en Flask con estructura modular, JWT (JSON Web Tokens), migraciones de base de datos y soporte para Docker. Ideal para proyectos educativos y prototipos rápidos.

✨ Características Principales

Flask organizado por módulos (models/, resources/, etc.).

SQLAlchemy + Flask-Migrate para versionar el esquema de la base de datos.

JWT con blocklist para invalidar tokens (logout/rotación).

Marshmallow (o esquemas en schema.py) para validación y serialización de datos.

Dockerfile para empaquetado y despliegue reproducible.

Soporte para variables de entorno vía .flaskenv/.env.

📁 Estructura del Proyecto
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

Por defecto: SQLite (sqlite:///data.db)

Producción: PostgreSQL o MySQL

⚙️ Configuración (Local)
1) Clonar e instalar dependencias
git clone https://github.com/Socrates-Programmer/Simple_API.git
cd Simple_API
python -m venv .venv


Activar entorno virtual

Windows (CMD/PowerShell):

.venv\Scripts\activate


Linux/Mac:

source .venv/bin/activate


Instalar dependencias

pip install -r requirements.txt

2) Variables de entorno

Crea un archivo .flaskenv en la raíz del proyecto (para desarrollo):

FLASK_APP=app.py
FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000

# Seguridad
JWT_SECRET_KEY=cambia-esto-por-un-secreto-seguro

# Base de datos
# Desarrollo (SQLite)
DATABASE_URL=sqlite:///data.db
# Producción (Postgres, ejemplo)
# DATABASE_URL=postgresql+psycopg2://user:pass@host:5432/dbname

3) Migraciones de base de datos
flask db upgrade

4) Ejecutar
flask run


Accede a: http://localhost:5000

🐳 Ejecutar con Docker

Build & Run (usando el dockerfile del repo):

docker build -t simple-api .
docker run --name simple-api \
  --env-file .flaskenv \
  -p 5000:5000 simple-api


(Opcional) Si agregas docker-compose.yml, puedes usar:

docker compose up --build

🔑 Autenticación (JWT)

Login: emite un access_token (y opcionalmente refresh_token).

Logout: agrega el token a la blocklist para invalidarlo inmediatamente.

⚠️ Producción: Guarda JWT_SECRET_KEY fuera del repositorio (secret manager/variables del entorno).

🔌 Endpoints (Plantilla)

Ajusta los paths/nombres según tus blueprints reales.

Método	Path	Descripción
GET	/	Health/Hello (estado del servicio)
POST	/auth/login	Recibe credenciales, responde con JWT
DELETE	/auth/logout	Invalida token activo (blocklist)
GET	/items	Lista de recursos
POST	/items	Crea recurso
GET	/items/<id>	Detalle de recurso
PUT	/items/<id>	Actualización de recurso
DELETE	/items/<id>	Borrado de recurso
🧪 Pruebas (Sugerencia)

Estructura sugerida

tests/
  ├─ conftest.py
  ├─ test_health.py
  └─ test_items.py


Ejecutar

pytest -q

♻️ Comandos de Migración
flask db init           # solo una vez (si no existe migrations/)
flask db migrate -m "mensaje"
flask db upgrade
flask db downgrade

📫 Contacto

Abre un Issue con tu duda o propuesta de mejora.

Email: marcosavila3005@gmail.com
