from fastapi import FastAPI
from app.database.db import Base, engine

# importar modelos
from app.models import client, order, inventory

# importar rutas
from app.controllers import client_controller, order_controller, dashboard_controller

from app.database.deps import SessionLocal
from app.models.inventory import Inventory

app = FastAPI()

# crear tablas
Base.metadata.create_all(bind=engine)

# registrar rutas
app.include_router(client_controller.router)

app.include_router(order_controller.router)

app.include_router(dashboard_controller.router)

def init_inventory():
    db = SessionLocal()
    inventory = db.query(Inventory).first()
    
    if not inventory:
        inventory = Inventory(total_gas=1000)  # ejemplo
        db.add(inventory)
        db.commit()
    
    db.close()

init_inventory()