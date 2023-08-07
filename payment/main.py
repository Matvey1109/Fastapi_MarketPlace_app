from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from payment.order.models import Order
from payment.order.schemas import OrderSchema
from payment.order.utils import get_db, get_order_util
from payment.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    return get_order_util(db, order_id)
