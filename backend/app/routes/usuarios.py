from fastapi import APIRouter, HTTPException
from app.database import usuarios_collection
from app.models.usuario import Usuario
from bson import ObjectId

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/")
def crear_usuario(usuario: Usuario):
    data = usuario.dict()
    result = usuarios_collection.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return data

@router.get("/")
def listar_usuarios():
    usuarios = []
    for usuario in usuarios_collection.find():
        usuario["_id"] = str(usuario["_id"])
        usuarios.append(usuario)
    return usuarios

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: str):
    usuario = usuarios_collection.find_one({"_id": ObjectId(usuario_id)})
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario["_id"] = str(usuario["_id"])
    return usuario

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: str):
    result = usuarios_collection.delete_one({"_id": ObjectId(usuario_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado"}
