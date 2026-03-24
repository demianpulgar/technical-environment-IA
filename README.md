# 🧠 Technical Environment IA

> **Entorno técnico completo de Python para Datos e Inteligencia Artificial**, desplegado como Web Service en [Render](https://render.com) con base de datos PostgreSQL administrada, desarrollado en Visual Studio Code y contenedorizado con Docker.

---

## 📋 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Stack Tecnológico](#-stack-tecnológico)
- [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
- [Estructura de Carpetas](#-estructura-de-carpetas)
- [Variables de Entorno](#-variables-de-entorno)
- [Endpoints de la API](#-endpoints-de-la-api)
- [Paso a Paso: Cómo se construyó este proyecto](#-paso-a-paso-cómo-se-construyó-este-proyecto)
- [Ejecución Local con Docker](#-ejecución-local-con-docker)
- [Despliegue en Render](#-despliegue-en-render)
- [Solución de Problemas](#-solución-de-problemas)

---

## 📌 Descripción General

Este proyecto establece la base de un entorno profesional para el desarrollo de aplicaciones orientadas a **datos e inteligencia artificial**. Incluye una API REST construida con **FastAPI**, conectada a una base de datos **PostgreSQL**, todo empaquetado en un contenedor **Docker** y desplegado en la nube mediante **Render**.

La arquitectura está pensada para escalar: el mismo código que corre en local con Docker Compose puede desplegarse directamente en producción sin modificaciones.

---

## 🛠 Stack Tecnológico

| Tecnología | Versión | Rol |
|---|---|---|
| **Python** | 3.11 | Lenguaje principal |
| **FastAPI** | 0.111.0 | Framework web / API REST |
| **Uvicorn** | 0.30.1 | Servidor ASGI |
| **SQLAlchemy** | 2.0.30 | ORM y gestión de conexiones |
| **psycopg2-binary** | 2.9.9 | Driver de PostgreSQL para Python |
| **python-dotenv** | 1.0.1 | Gestión de variables de entorno |
| **PostgreSQL** | 15 / Render Managed | Base de datos relacional |
| **Docker** | — | Contenedorización |
| **Docker Compose** | — | Orquestación local |
| **Render** | — | Plataforma de despliegue en la nube |
| **Visual Studio Code** | — | IDE de desarrollo |
| **Git + GitHub** | — | Control de versiones |

---

## 🏗 Arquitectura del Proyecto

```
┌─────────────────────────────────────────────────────┐
│                     RENDER CLOUD                    │
│                                                     │
│  ┌──────────────────┐      ┌──────────────────────┐ │
│  │   Web Service    │      │  PostgreSQL (Managed) │ │
│  │  FastAPI + Uvi.  │─────▶│   Render Database    │ │
│  │   Puerto 8000    │      │    Puerto 5432        │ │
│  └──────────────────┘      └──────────────────────┘ │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│                  ENTORNO LOCAL                      │
│                                                     │
│  ┌──────────────────┐      ┌──────────────────────┐ │
│  │  Docker: api     │      │   Docker: db         │ │
│  │  FastAPI + Uvi.  │─────▶│   postgres:15        │ │
│  │   Puerto 8000    │      │    Puerto 5432        │ │
│  └──────────────────┘      └──────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

---

## 📁 Estructura de Carpetas

```
mi-entorno-ia/
│
├── app/                        # Paquete principal de la aplicación
│   ├── __init__.py             # Marca el directorio como módulo Python
│   ├── main.py                 # Definición de la app FastAPI y endpoints
│   └── db.py                   # Engine de SQLAlchemy + gestión de sesiones
│
├── .env                        # Variables de entorno locales (NO commitear)
├── .env.example                # Plantilla de variables de entorno
├── .gitignore                  # Archivos excluidos del repositorio
├── Dockerfile                  # Imagen Docker de la aplicación
├── docker-compose.yml          # Orquestación local (api + postgres)
├── requirements.txt            # Dependencias Python
└── README.md                   # Este archivo
```

---

## 🔐 Variables de Entorno

El proyecto utiliza un archivo `.env` para gestionar la configuración sensible. **Este archivo nunca debe subirse a GitHub** (ya está incluido en `.gitignore`).

### `.env.example` — Plantilla

```env
DATABASE_URL=postgresql://user:password@host:port/database
```

### `.env` — Uso local

```env
# Formato para conexión a PostgreSQL local (Docker Compose)
DATABASE_URL=postgresql://usuario:password@db:5432/entorno_ia

# Formato para conexión a Render (producción)
DATABASE_URL=postgresql://user:pass@host/dbname?sslmode=require
```

> ⚠️ **En Render:** La variable `DATABASE_URL` se configura directamente en el dashboard del servicio bajo la sección **Environment**, nunca en el código fuente.

---

## 🔗 Endpoints de la API

### `GET /`

Verifica que el servicio esté activo.

**Respuesta exitosa `200 OK`:**
```json
{
  "status": "ok",
  "message": "API de Entorno de Datos e IA funcionando correctamente"
}
```

---

### `GET /health/db`

Ejecuta `SELECT 1` para verificar la conectividad con la base de datos PostgreSQL.

**Respuesta exitosa `200 OK`:**
```json
{
  "status": "ok",
  "database": "connected",
  "message": "Conexión a PostgreSQL exitosa"
}
```

**Respuesta de error `503 Service Unavailable`:**
```json
{
  "detail": {
    "status": "error",
    "database": "disconnected",
    "message": "Error de conexión a PostgreSQL: ..."
  }
}
```

---

### Documentación interactiva

FastAPI genera automáticamente documentación interactiva:

| Interfaz | URL |
|---|---|
| **Swagger UI** | `http://localhost:8000/docs` |
| **ReDoc** | `http://localhost:8000/redoc` |
| **OpenAPI JSON** | `http://localhost:8000/openapi.json` |

---

## 🚶 Paso a Paso: Cómo se construyó este proyecto

### 1. Configuración del entorno de desarrollo en VS Code

Se utilizó **Visual Studio Code** como IDE principal. El proyecto se organizó en el directorio de trabajo local y se configuró Git para control de versiones.

```
Herramientas instaladas:
- Python 3.11
- Docker Desktop
- Git
- Visual Studio Code
```

---

### 2. Creación de la estructura del proyecto

Se creó manualmente la siguiente estructura de carpetas y archivos base:

```
mi-entorno-ia/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── db.py
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

### 3. Definición de dependencias (`requirements.txt`)

Se especificaron las dependencias con versiones fijas para garantizar reproducibilidad:

```
fastapi==0.111.0
uvicorn==0.30.1
psycopg2-binary==2.9.9
sqlalchemy==2.0.30
python-dotenv==1.0.1
```

> **Decisión técnica:** Se utilizó `psycopg2-binary` en lugar de `psycopg2` porque incluye las dependencias del sistema pre-compiladas, lo que evita errores de compilación en imágenes Docker slim como `python:3.11-slim`.

---

### 4. Configuración de la base de datos (`app/db.py`)

Se implementó el motor de SQLAlchemy que lee la URL de conexión desde las variables de entorno mediante `python-dotenv`:

```python
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

> **`pool_pre_ping=True`**: SQLAlchemy verifica la conexión antes de usarla, evitando errores por conexiones caídas o timeouts en la nube.

---

### 5. Creación de la API (`app/main.py`)

Se construyó la aplicación FastAPI con dos endpoints:

- **`GET /`** → Responde con el estado general del servicio.
- **`GET /health/db`** → Ejecuta `SELECT 1` contra PostgreSQL para verificar la conexión en tiempo real.

---

### 6. Dockerización

#### `Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

> **Decisión técnica:** Se usa `python:3.11-slim` (imagen mínima de Debian) para reducir el tamaño de la imagen al mínimo necesario. `--no-cache-dir` evita almacenar el caché de pip en la imagen.

#### `docker-compose.yml`

Define dos servicios para desarrollo local:

- **`api`**: construida desde el `Dockerfile` local, expone el puerto `8000`.
- **`db`**: imagen oficial `postgres:15` con volumen persistente en `pg_data`.

---

### 7. Gestión de variables de entorno

Se creó un `.env` con la `DATABASE_URL` y un `.env.example` como plantilla para colaboradores. El `.gitignore` excluye `.env` para que las credenciales nunca lleguen al repositorio.

---

### 8. Inicialización del repositorio Git

```bash
git init
git add .
git commit -m "feat: estructura inicial del entorno de datos e IA"
```

---

### 9. Publicación en GitHub

Se vinculó el repositorio local con el repositorio remoto en GitHub y se realizó el push inicial:

```bash
git remote add origin https://github.com/demianpulgar/technical-environment-IA.git
git branch -M main
git push -u origin main
```

---

### 10. Creación de la base de datos PostgreSQL en Render

1. Ingresar a [render.com](https://render.com) → **New → PostgreSQL**
2. Configurar:
   - **Name:** `entorno_ia`
   - **Database:** `entorno_ia`
   - **User:** `usuario`
   - **Region:** el más cercano a tu ubicación
3. Render genera automáticamente la **Internal Database URL** y la **External Database URL**
4. Copiar la **Internal Database URL** para usarla en el Web Service

---

### 11. Creación del Web Service en Render

1. En Render → **New → Web Service**
2. Conectar el repositorio de GitHub: `demianpulgar/technical-environment-IA`
3. Configurar:
   - **Runtime:** Docker
   - **Branch:** `main`
   - **Dockerfile Path:** `./Dockerfile`
4. En la sección **Environment**, agregar la variable:
   ```
   DATABASE_URL = <Internal Database URL de Render con ?sslmode=require>
   ```
5. Hacer clic en **Deploy**

---

### 12. Resolución de errores en el despliegue

Durante el proceso de despliegue en Render se identificaron y corrigieron los siguientes problemas:

#### ❌ Error 1: versión de `psycopg2` incorrecta
```
ERROR: Could not find a version that satisfies the requirement psycopg2==1.1.1
```
**Causa:** `psycopg2==1.1.1` no existe en PyPI.  
**Solución:** Se reemplazó por `psycopg2-binary==2.9.9`.

#### ❌ Error 2: `version` obsoleto en `docker-compose.yml`
```
the attribute `version` is obsolete, it will be ignored
```
**Causa:** Las versiones modernas de Docker Compose deprecaron el campo `version`.  
**Solución:** Se eliminó el campo `version` del archivo.

#### ❌ Error 3: Conexión SSL requerida por Render
**Causa:** Render exige conexiones cifradas a su PostgreSQL administrado.  
**Solución:** Se agregó `?sslmode=require` al final de la `DATABASE_URL`.

---

## 🐳 Ejecución Local con Docker

### Prerrequisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución
- Archivo `.env` configurado con las credenciales correctas

### Comandos

```bash
# Clonar el repositorio
git clone https://github.com/demianpulgar/technical-environment-IA.git
cd technical-environment-IA

# Copiar y configurar el archivo de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Construir e iniciar todos los servicios
docker-compose up -d

# Ver los logs en tiempo real
docker-compose logs -f

# Verificar que los contenedores estén corriendo
docker-compose ps

# Detener y eliminar los contenedores
docker-compose down

# Detener y eliminar contenedores + volúmenes (borra los datos)
docker-compose down -v
```

### URLs en local

| Recurso | URL |
|---|---|
| API raíz | http://localhost:8000/ |
| Health check DB | http://localhost:8000/health/db |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

## ☁️ Despliegue en Render

### Prerrequisitos

- Cuenta en [render.com](https://render.com)
- Repositorio en GitHub conectado a Render

### Configuración de variables de entorno en Render

En el dashboard de Render → tu Web Service → **Environment**:

```
DATABASE_URL = postgresql://user:pass@host/dbname?sslmode=require
```

> Usar siempre la **Internal Database URL** si el Web Service y la base de datos están en el mismo proyecto de Render. Esto mejora la latencia y evita costos adicionales de transferencia.

### Deploy automático

Render detecta automáticamente cada push a la rama `main` y realiza un nuevo despliegue. No se requiere ninguna acción manual adicional.

---

## 🔧 Solución de Problemas

| Problema | Causa probable | Solución |
|---|---|---|
| `open //./pipe/dockerDesktopLinuxEngine` | Docker Desktop no está corriendo | Abrir Docker Desktop y esperar a que inicie |
| `psycopg2==1.1.1` no encontrado | Versión inexistente en PyPI | Usar `psycopg2-binary==2.9.9` |
| Error SSL en la conexión | Render requiere SSL | Agregar `?sslmode=require` a la URL |
| `version` obsoleto en compose | Docker Compose moderno | Eliminar el campo `version` del archivo |
| Push rechazado (`fetch first`) | El remoto tiene cambios locales no presentes | Hacer `git pull` o `git push --force` |

---

## 🤝 Contribuciones

1. Hacer fork del repositorio
2. Crear una rama: `git checkout -b feature/nueva-funcionalidad`
3. Realizar los cambios y hacer commit: `git commit -m "feat: descripción"`
4. Hacer push: `git push origin feature/nueva-funcionalidad`
5. Abrir un Pull Request

---

## 📄 Licencia

MIT License — libre para uso personal y comercial.
