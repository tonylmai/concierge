from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database (for demonstration purposes)
items = []

# Pydantic model for item data
class Item(BaseModel):
    name: str
    description: str


# Get all items in database
@app.get("/items/")
async def get_all_items():
    '''
     Get all the items from databaser 
    '''
    return items


# Create an item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

# Get an item by ID
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


# Update an item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    items[item_id] = item
    return item


# Delete an item
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = items.pop(item_id)
    return deleted_item


# We will start the server without the need to specify "mainl:app" 
#  where 'main' refers to the file main.py 
#  and 'app' for the variable name pointing to FastAPI object

if __name__ == "__main__":
    ## start FastAPI server
    import uvicorn
    uvicorn.run("main:app", reload=True)
    