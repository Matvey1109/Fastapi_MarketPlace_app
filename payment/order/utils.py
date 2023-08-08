from sqlalchemy.orm import Session
from payment.order.models import Order
from payment.order.schemas import OrderSchema
from payment.database import SessionLocal
import requests


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_order_util(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def add_order_to_db_util(db: Session, order: Order):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def order_completed(db: Session, order_id: int):
    order = db.query(Order).get(order_id)
    if order:
        order.status = "completed"
        db.commit()
