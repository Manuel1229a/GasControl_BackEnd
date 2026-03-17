from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.order import Order
from app.models.inventory import Inventory

def get_dashboard(db: Session):
    # Total pedidos
    total_orders = db.query(func.count(Order.id)).scalar()

    # Total vendido
    total_revenue = db.query(func.sum(Order.total_price)).scalar()

    # Gas restante
    inventory = db.query(Inventory).first()

    return {
        "total_orders": total_orders or 0,
        "total_revenue": total_revenue or 0,
        "total_gas": inventory.total_gas if inventory else 0
    }