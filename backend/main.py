from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List, Optional
import os
import json
from .models import Product

app = FastAPI(title="Gestion de Produits API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products_db = []
id_counter = 1

def load_initial_data():
    global id_counter, products_db
    json_path = os.path.join(os.path.dirname(__file__), "products.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                products_db = [Product(**item) for item in data]
                if products_db:
                    id_counter = max(p.id for p in products_db) + 1
        except Exception as e:
            pass

load_initial_data()

@app.get("/products", response_model=List[Product])
def get_products():
    return products_db

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = next((p for p in products_db if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return product

@app.post("/products", response_model=Product, status_code=201)
def create_product(product: Product):
    global id_counter
    product.id = id_counter
    products_db.append(product)
    id_counter += 1
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    index = next((i for i, p in enumerate(products_db) if p.id == product_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    
    updated_product.id = product_id
    products_db[index] = updated_product
    return updated_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    index = next((i for i, p in enumerate(products_db) if p.id == product_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    
    products_db.pop(index)
    return {"message": "Produit supprimé avec succès"}

frontend_path = os.path.join(os.getcwd(), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

    @app.get("/")
    async def read_index():
        return FileResponse(os.path.join(frontend_path, "index.html"))
