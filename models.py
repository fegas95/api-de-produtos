from pydantic import BaseModel, Field
from typing import Optional


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="Notebook Dell")
    description: Optional[str] = Field(None, max_length=300, example="Intel i5, 8GB RAM, 256GB SSD")
    price: float = Field(..., gt=0, example=2999.90)
    stock: int = Field(..., ge=0, example=10)


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: int

    class Config:
        from_attributes = True
