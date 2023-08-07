from sqlalchemy import Column, Integer, Float, String
from inventory.database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Float)
    quantity = Column(Integer)
