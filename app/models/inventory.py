from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from app.database.db import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    total_gas = Column(Float, default=0)
    updated_at = Column(DateTime, default=datetime.utcnow)