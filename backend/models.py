from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    nom: str
    description: str
    prix: float
    quantite: int
