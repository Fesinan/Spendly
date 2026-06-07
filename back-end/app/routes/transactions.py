from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Transaction
from ..schemas import TransactionCreate, TransactionOut

router = APIRouter(prefix="/api/transactions", tags=["transactions"])


@router.get("/", response_model=list[TransactionOut])
def list_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).order_by(Transaction.created_at.desc()).all()


@router.post("/", response_model=TransactionOut, status_code=201)
def create_transaction(body: TransactionCreate, db: Session = Depends(get_db)):
    tx = Transaction(**body.model_dump())
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx


@router.get("/{tx_id}", response_model=TransactionOut)
def get_transaction(tx_id: int, db: Session = Depends(get_db)):
    tx = db.get(Transaction, tx_id)
    if tx is None:
        from fastapi import HTTPException
        raise HTTPException(404, "Transaction not found")
    return tx
