from fastapi import FastAPI
from app.routes import libros, usuarios, prestamos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API de Préstamos")

# Permitir llamadas desde el frontend (dev)
origins = [
    "http://localhost:5173",  # Vite default dev port
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(libros.router)
app.include_router(usuarios.router)
app.include_router(prestamos.router)

@app.get("/")
def root():
    return {"message": "API de Préstamos activa ✅"}
