from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.services.dashboard_service import get_dashboard
from app.schemas.dashboard_schema import DashboardResponse

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/", response_model=DashboardResponse)
def read_dashboard(db: Session = Depends(get_db)):
    return get_dashboard(db)