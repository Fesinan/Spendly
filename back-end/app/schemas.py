import datetime

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    description: str
    amount: float
    category: str | None = None


class TransactionOut(BaseModel):
    id: int
    description: str
    amount: float
    category: str | None
    created_at: datetime.datetime

    model_config = {"from_attributes": True}
