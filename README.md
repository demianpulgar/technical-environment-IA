# Mi Entorno IA

Entorno completo de Python para desarrollo de aplicaciones de Datos e Inteligencia Artificial.

## 🚀 Tecnologías

- **FastAPI** - Framework web moderno y de alto rendimiento
- **SQLAlchemy** - ORM para Python
- **MySQL** - Base de datos relacional
- **Docker** - Contenedorización
- **Uvicorn** - Servidor ASGI

## 📁 Estructura del Proyecto

```
mi-entorno-ia/
├── app/
│   ├── __init__.py
│   ├── main.py          # Endpoints de la API
│   └── db.py            # Configuración de base de datos
├── .env                 # Variables de entorno (no commitear)
├── .env.example         # Ejemplo de variables de entorno
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## ⚙️ Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd mi-entorno-ia
   ```

2. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
   ```

3. **Iniciar con Docker:**
   ```bash
   docker-compose up -d
   ```

## 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Estado de la API |
| GET | `/health/db` | Verificar conexión a MySQL |

## 📝 Uso

### Con Docker (recomendado)

```bash
# Construir e iniciar los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down
```

### Sin Docker

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
uvicorn app.main:app --reload
```

## 🌐 Acceso

- **API:** http://localhost:8000
- **Documentación Swagger:** http://localhost:8000/docs
- **Documentación ReDoc:** http://localhost:8000/redoc

## 📄 Licencia

MIT License
