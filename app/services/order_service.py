from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.client import Client
from app.models.inventory import Inventory
from fastapi import HTTPException

def create_order(db: Session, data):
    # 1. Validar cliente
    client = db.query(Client).filter(Client.id == data.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # 2. Obtener inventario (solo 1 registro)
    inventory = db.query(Inventory).first()
    if not inventory:
        raise HTTPException(status_code=400, detail="Inventario no inicializado")

    # 3. Validar gas disponible
    if inventory.total_gas < data.liters:
        raise HTTPException(status_code=400, detail="Gas insuficiente")

    # 4. Calcular precio
    total_price = data.liters * data.price_per_liter

    # 5. Crear pedido
    new_order = Order(
        client_id=data.client_id,
        liters=data.liters,
        total_price=total_price
    )

    # 6. Descontar gas
    inventory.total_gas -= data.liters

    # 7. Guardar todo
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order