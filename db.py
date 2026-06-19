import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

conexion = None


def get_conexion():
    global conexion
    if conexion is None:
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={os.getenv('DB_SERVER')};DATABASE={os.getenv('DB_DATABASE')};"
            f"UID={os.getenv('DB_USER')};PWD={os.getenv('DB_PASSWORD')}"
        )
    return conexion
