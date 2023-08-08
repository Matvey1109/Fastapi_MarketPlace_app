from fastapi import FastAPI, Depends, Request, HTTPException, status
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
async def create_order(product_id: int, quantity: int, background_task: BackgroundTasks, db: Session = Depends(get_db)):
    req = requests.get(f"http://localhost:8000/products/{product_id}")
    product = req.json()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The product is not found")

    if product["quantity"] < quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient quantity available")

    order = Order(
        product_id=product_id,
        price=product["price"],
        fee=0.2 * product["price"],
        total=1.2 * product["price"],
        quantity=quantity,
        status="pending",
    )

    add_order_to_db_util(db, order)
    background_task.add_task(order_completed, db, order.id)

    new_quantity = product["quantity"] - quantity
    requests.put(f"http://localhost:8000/products/{product_id}/{new_quantity}")

    return order
