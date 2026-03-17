from pydantic import BaseModel

class OrderCreate(BaseModel):
    client_id: int
    liters: float
    price_per_liter: float

class OrderResponse(BaseModel):
    id: int
    client_id: int
    liters: float
    total_price: float

    class Config:
        from_attributes = True