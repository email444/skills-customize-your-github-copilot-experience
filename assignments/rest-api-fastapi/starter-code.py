from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(title="Item Store API", version="1.0.0")

# Pydantic model for Item
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


# In-memory database for items (replace with a real database later)
items_db = {
    1: Item(name="Laptop", price=999.99, description="A powerful laptop"),
    2: Item(name="Mouse", price=29.99),
    3: Item(name="Keyboard", price=79.99, description="Mechanical keyboard"),
}


# TODO: Implement the GET endpoint at "/" that returns a welcome message
@app.get("/")
async def read_root():
    pass


# TODO: Implement the GET endpoint at "/items/" that returns all items
@app.get("/items/")
async def read_items():
    pass


# TODO: Implement the GET endpoint at "/items/{item_id}" that returns a specific item
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    pass


# TODO: Implement the POST endpoint at "/items/" to create a new item
@app.post("/items/")
async def create_item(item: Item):
    pass


# TODO: Implement the PUT endpoint at "/items/{item_id}" to update an item
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    pass


# TODO: Implement the DELETE endpoint at "/items/{item_id}" to delete an item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    pass


# To run the application:
# uvicorn main:app --reload
# Then visit http://localhost:8000/docs to see the interactive API documentation
