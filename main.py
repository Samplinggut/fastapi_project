from typing import Union

from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


#@app.get("/", response_class=HTMLResponse)
#async def read_item(request: Request):
#    return templates.TemplateResponse(
 #       request=request, name="index.html")

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
 #   return {"item_id": item_id, "q": q} 
# ✅ Define a Pydantic model for input/output
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

# ✅ Basic GET route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# ✅ GET with query parameters
@app.get("/search")
def search_items(name: str, limit: int = 10):
    return {"search_for": name, "limit": limit}

# ✅ GET with path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

# ✅ POST: create a new item
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created", "item": item}

# ✅ PUT: update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": "Item updated", "item_id": item_id, "item": item}

# ✅ DELETE: delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with ID {item_id} deleted"}