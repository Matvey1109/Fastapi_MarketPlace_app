from sqlalchemy.orm import Session
from inventory.product.models import Product
from inventory.product.schemas import ProductSchema
from inventory.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_product_util(db: Session, product: ProductSchema):
    product = Product(name=product.name, price=product.price, quantity=product.quantity)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_product_util(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def all_products_util(db: Session):
    products = db.query(Product)
    return [get_product_util(db, p.id) for p in products]


def del_product_util(db: Session, product_id: int):
    product = db.query(Product).get(product_id)
    if product:
        db.delete(product)
        db.commit()
        return True
    return False
