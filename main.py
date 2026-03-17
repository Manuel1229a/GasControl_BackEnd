from fastapi import FastAPI
from app.database.db import Base, engine

# importar modelos
from app.models import client, order, inventory

# importar rutas
from app.controllers import client_controller

app = FastAPI()

# crear tablas
Base.metadata.create_all(bind=engine)

# registrar rutas
app.include_router(client_controller.router)