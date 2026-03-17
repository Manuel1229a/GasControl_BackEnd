from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.schemas.order_schema import OrderCreate, OrderResponse
from app.services.order_service import create_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderResponse)
def create(data: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, data)