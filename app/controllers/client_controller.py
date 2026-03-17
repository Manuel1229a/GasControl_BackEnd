from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.schemas.client_schema import ClientCreate, ClientResponse
from app.services.client_service import create_client, get_clients

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.post("/", response_model=ClientResponse)
def create(data: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, data)

@router.get("/", response_model=list[ClientResponse])
def read(db: Session = Depends(get_db)):
    return get_clients(db)