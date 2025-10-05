
from dataclasses import dataclass

@dataclass
class Car:
    model: str
    year: int
    color: str
    speed: float
    csrfmiddlewaretoken: str = None
    
#models.Model