from pydantic import BaseModel

class DashboardResponse(BaseModel):
    total_orders: int
    total_revenue: float
    total_gas: float