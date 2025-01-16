from fastapi import FastAPI
import uvicorn
import requests

# Crear una aplicación FastAPI simple
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI y Uvicorn están funcionando correctamente"}

if __name__ == "__main__":
    print("✅ FastAPI y Uvicorn están configurados y el servidor está en ejecución.")
    print("💻 Abre tu navegador y visita: http://127.0.0.1:8000")
    # Inicia el servidor de Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
