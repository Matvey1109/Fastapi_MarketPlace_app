from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from inventory.product.models import Product
from inventory.product.schemas import ProductSchema
from inventory.product.utils import get_db, create_product_util, get_product_util, all_products_util, del_product_util, \
    change_product_quantity_util
from inventory.database import Base, engine
import requests

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/products")
def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    return create_product_util(db, product)


@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_util(db, product_id)


@app.put("/products/{product_id}/{quantity}")
def change_product_quantity(product_id: int, quantity: int, db: Session = Depends(get_db)):
    return change_product_quantity_util(db, product_id, quantity)


@app.get("/products")
def all_products(db: Session = Depends(get_db)):
    return all_products_util(db)


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return del_product_util(db, product_id)
