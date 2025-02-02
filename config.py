from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_SERVER = os.getenv("python-crud-server.database.windows.net")
DATABASE_NAME = os.getenv("python-crud-db")
DATABASE_USERNAME = os.getenv("rakesh")
DATABASE_PASSWORD = os.getenv("python_crud_123")

def get_connection_string():
    return f"Driver={{ODBC Driver 17 for SQL Server}};Server=python-crud-server.database.windows.net;Database=python-crud-db;UID=rakesh;PWD=python_crud_123"
