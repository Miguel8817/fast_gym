from fastapi import APIRouter, HTTPException, Form
from pydantic import BaseModel
from repositorios import EliminarRepository, InsertarRepository, EditarRepository, ObtenerRepository
from typing import Annotated
router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

class DatosUser(BaseModel):
    name: str
    email: str
    password: str

@router.post("/Registro/{id_users}") 
def Registrarse(id_users: int, 
                name: str = Form(...), 
                email: str = Form(...), 
                password: str = Form(...)):
    try:
        usuarios = InsertarRepository.Insert(id_users, name, email, password)
        return usuarios
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al insertar: {e}")


@router.put("/actualizar_user/{id_users}")
def Act_user(id_users: int, data: DatosUser):
    try:
        usuarios = EditarRepository.Edit_user(id_users, data.name, data.email, data.password)
        return usuarios
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {e}")


@router.delete("/delete_users/{id_users}")
def delete_user(id_users: int):
    try:
        usuario = EliminarRepository.Eliminar_Usuarios(id_users)
        return usuario
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"No se pudo borrar el usuario: {e}")


@router.get("/Obtener_users")
def obtener_users():
    try:
        usuarios = ObtenerRepository.Obtener_user()
        return usuarios
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los usuarios: {e}")
