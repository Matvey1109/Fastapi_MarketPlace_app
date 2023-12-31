from pydantic import BaseModel


class OrderSchema(BaseModel):
    id: int
    product_id: int
    price: float
    fee: float
    total: float
    quantity: int
    status: str
