from fastapi import FastAPI, HTTPException
import pyodbc
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Database connection
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=python-crud-server.database.windows.net;Database=python-crud-db;UID=rakesh;PWD=Raki@054"

class Item(BaseModel):
    name: str
    description: str

@app.get("/items")
def read_items():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return items

@app.post("/items")
def create_item(item: Item):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, description) VALUES (?, ?)",
        item.name,
        item.description
    )
    conn.commit()
    conn.close()
    return {"message": "Item created successfully"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET name=?, description=? WHERE id=?",
        item.name,
        item.description,
        item_id
    )
    conn.commit()
    conn.close()
    return {"message": "Item updated successfully"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id=?", item_id)
    conn.commit()
    conn.close()
    return {"message": "Item deleted successfully"}
