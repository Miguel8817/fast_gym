import pyodbc
from db import conexion


def transaction(func):
    def wrapper(*args, **kwargs):
        try:
            resultado = func(*args, **kwargs)
            conexion.commit()
            return resultado
        except pyodbc.Error:
            conexion.rollback()
            raise
    return wrapper
