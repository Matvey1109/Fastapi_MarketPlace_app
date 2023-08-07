from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    price: float
    quantity: int
