from sqlalchemy import Column, Integer, Float, String
from payment.database import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    fee = Column(Float)
    total = Column(Float)
    quantity = Column(Integer)
    status = Column(String)
