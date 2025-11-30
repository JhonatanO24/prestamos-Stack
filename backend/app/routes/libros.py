from fastapi import APIRouter, HTTPException
from app.database import libros_collection
from app.models.libro import Libro
from bson import ObjectId

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/")
def crear_libro(libro: Libro):
    data = libro.dict()
    result = libros_collection.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return data

@router.get("/")
def listar_libros():
    libros = []
    for libro in libros_collection.find():
        libro["_id"] = str(libro["_id"])
        libros.append(libro)
    return libros

@router.get("/{libro_id}")
def obtener_libro(libro_id: str):
    libro = libros_collection.find_one({"_id": ObjectId(libro_id)})
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    libro["_id"] = str(libro["_id"])
    return libro

@router.delete("/{libro_id}")
def eliminar_libro(libro_id: str):
    result = libros_collection.delete_one({"_id": ObjectId(libro_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"message": "Libro eliminado"}
