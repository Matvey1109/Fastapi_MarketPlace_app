from fastapi import FastAPI, Depends, Request, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from sqlalchemy.orm import Session
from payment.order.models import Order
from payment.order.schemas import OrderSchema
from payment.order.utils import get_db, get_order_util, add_order_to_db_util, order_completed
from payment.database import Base, engine
import requests

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


@app.post("/orders")
async def create_order(id: int, quantity: int, background_task: BackgroundTasks, db: Session = Depends(get_db)):
    req = requests.get(f"http://localhost:8000/products/{id}")
    product = req.json()

    if product["quantity"] < quantity:
        raise HTTPException(status_code=400, detail="Insufficient quantity available")

    order = Order(
        product_id=id,
        price=product["price"],
        fee=0.2 * product["price"],
        total=1.2 * product["price"],
        quantity=quantity,
        status="pending",
    )

    add_order_to_db_util(db, order)
    background_task.add_task(order_completed, db, order.id)

    return order
