from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_SERVER = os.getenv("DATABASE_SERVER")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

def get_connection_string():
    return f"Driver={{ODBC Driver 17 for SQL Server}};Server=python-crud-server.database.windows.net;Database=python-crud-db;UID=;PWD="
