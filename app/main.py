from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from app.db import engine

app = FastAPI(
    title="Entorno de Datos e IA",
    description="API para gestión de datos e inteligencia artificial",
    version="1.0.0"
)


@app.get("/")
def root():
    """Endpoint raíz que retorna el estado de la API."""
    return {
        "status": "ok",
        "message": "API de Entorno de Datos e IA funcionando correctamente"
    }


@app.get("/health/db")
def health_db():
    """Endpoint para verificar la conexión a la base de datos MySQL."""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "status": "ok",
            "database": "connected",
            "message": "Conexión a MySQL exitosa"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "error",
                "database": "disconnected",
                "message": f"Error de conexión a MySQL: {str(e)}"
            }
        )
