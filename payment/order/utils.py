from sqlalchemy.orm import Session
from payment.order.models import Order
from payment.order.schemas import OrderSchema
from payment.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_order_util(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()
