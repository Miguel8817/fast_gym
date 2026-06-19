import pyodbc
from db import get_conexion


class EliminarRepository:
    @staticmethod
    def Eliminar_Usuarios(id_user: int):
        conexion = get_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "DELETE FROM usuarios WHERE id_user = ?", (id_user,)
            )
            conexion.commit()
            return {"message": "Usuario eliminado"}
        except pyodbc.Error as e:
            conexion.rollback()
            raise e
        finally:
            cursor.close()


class InsertarRepository:
    @staticmethod
    def Insert(id_users: int, name: str, email: str, password: str):
        conexion = get_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (id_users, name, email, password) VALUES (?, ?, ?, ?)",
                (id_users, name, email, password)
            )
            conexion.commit()
            return {"message": "Insertado con éxito"}
        except pyodbc.Error as e:
            conexion.rollback()
            raise e
        finally:
            cursor.close()


class EditarRepository:
    @staticmethod
    def Edit_user(id_users: int, name: str, email: str, password: str):
        conexion = get_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "UPDATE usuarios SET name = ?, email = ?, password = ? WHERE id_user = ?",
                (name, email, password, id_users)
            )
            conexion.commit()
            return {"message": "Usuario actualizado"}
        except pyodbc.Error as e:
            conexion.rollback()
            raise e
        finally:
            cursor.close()


class ObtenerRepository:
    @staticmethod
    def Obtener_user():
        conexion = get_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in usuarios]
        except pyodbc.Error as e:
            raise e
        finally:
            cursor.close()
