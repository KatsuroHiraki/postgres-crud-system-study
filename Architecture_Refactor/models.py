from dataclasses import dataclass
from typing import Optional

@dataclass
class Product :
    product_name : str
    price: float
    stock_quantity : int
    product_id : Optional[int] = None