##################imports##################################

from pydantic import BaseModel              #validación de datos (?)
from datetime import datetime               #función para el tipo de dato DATE, DATETIME
from datetime import date

class RecordIn (BaseModel):
    categoria: str
    tipo: str 
    cantidad: float
    fecha_registro: date #revise

class RecordOut (BaseModel):
    id: int = 0 
    categoria: str
    tipo: str 
    cantidad: float
    fecha_registro: date #revise