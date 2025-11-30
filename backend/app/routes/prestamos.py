from fastapi import APIRouter, HTTPException
from app.database import prestamos_collection, libros_collection, usuarios_collection
from app.models.prestamo import Prestamo
from app.services.retraso_service import calcular_retraso_en_dias
from bson import ObjectId
from datetime import datetime

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.get("/")
def listar_prestamos():
    pipeline = [
        {
            "$match": {
                "fecha_devolucion_real": None
            }
        },
        # Ahora el resto del pipeline original para hacer los joins (lookups)
        {
            "$lookup": {
                "from": "usuarios",
                "localField": "usuario_id",
                "foreignField": "_id",
                "as": "usuario_info"
            }
        },
        {
            "$unwind": {
                "path": "$usuario_info",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$lookup": {
                "from": "libros",
                "localField": "libro_id",
                "foreignField": "_id",
                "as": "libro_info"
            }
        },
        {
            "$unwind": {
                "path": "$libro_info",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$project": {
                "_id": {"$toString": "$_id"},

                "usuario_id": {"$toString": "$usuario_id"},
                "libro_id": {"$toString": "$libro_id"},

                "fecha_prestamo": 1,
                "fecha_devolucion_esperada": 1,
                "fecha_devolucion_real": 1,
                "retraso_dias": 1,

                "usuario": {
                    "id": {"$toString": "$usuario_info._id"},
                    "nombre": {"$ifNull": ["$usuario_info.nombre", "Desconocido"]}
                },
                "libro": {
                    "id": {"$toString": "$libro_info._id"},
                    "titulo": {"$ifNull": ["$libro_info.titulo", "Desconocido"]}
                }
            }
        }
    ]

    prestamos = list(prestamos_collection.aggregate(pipeline))
    return prestamos

@router.post("/")
def crear_prestamo(prestamo: Prestamo):
    try:
        usuario_oid = ObjectId(prestamo.usuario_id)
        libro_oid = ObjectId(prestamo.libro_id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de Usuario o Libro con formato inválido")

    usuario = usuarios_collection.find_one({"_id": usuario_oid})
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no existe")

    libro = libros_collection.find_one({"_id": libro_oid})
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no existe")

    if libro.get("disponible") == False:
        raise HTTPException(status_code=400, detail="Libro no disponible")

    libros_collection.update_one(
        {"_id": libro_oid},
        {"$set": {"disponible": False}}
    )

    data = prestamo.dict()
    data["usuario_id"] = usuario_oid  # Asegura que el ID se guarde como ObjectId
    data["libro_id"] = libro_oid  # Asegura que el ID se guarde como ObjectId

    result = prestamos_collection.insert_one(data)
    data["_id"] = str(result.inserted_id)
    data["usuario_id"] = str(data["usuario_id"])
    data["libro_id"] = str(data["libro_id"])

    return data

@router.put("/devolucion/{prestamo_id}")
def devolver_libro(prestamo_id: str):
    try:
        prestamo_oid = ObjectId(prestamo_id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de Préstamo con formato inválido")

    prestamo = prestamos_collection.find_one({"_id": prestamo_oid})
    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no existe")

    fecha_real = datetime.now()
    fecha_esperada = prestamo.get("fecha_devolucion_esperada")

    if not fecha_esperada:
        dias_retraso = 0
    else:
        dias_retraso = calcular_retraso_en_dias(fecha_esperada, fecha_real)

    prestamos_collection.update_one(
        {"_id": prestamo_oid},
        {"$set": {"fecha_devolucion_real": fecha_real, "retraso_dias": dias_retraso}}
    )

    libros_collection.update_one(
        {"_id": prestamo.get("libro_id")},
        {"$set": {"disponible": True}}
    )

    return {
        "message": "Libro devuelto correctamente",
        "retraso_dias": dias_retraso
    }