import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, func

from .database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(100), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
