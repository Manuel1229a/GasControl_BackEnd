from sqlalchemy.orm import Session
from app.models.client import Client

def create_client(db: Session, data):
    new_client = Client(**data.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_clients(db: Session):
    return db.query(Client).all()