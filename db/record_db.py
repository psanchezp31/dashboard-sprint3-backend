##################imports##################################

from typing import Dict  # tipado de datos (ej: str, int, boolean, etc.)
from pydantic import BaseModel  # validación de datos (?)
from datetime import datetime  # función para el tipo de dato DATE, DATETIME
from datetime import date
###########definición de el objeto record##################


class RecordInDB(BaseModel):
    id: int = 0  # AUTOINCREMENTAL
    categoria: str  # e.g. HEALTH, PETS, FOOD, SALARY
    tipo: str  # EXPENSES OR INCOME
    cantidad: float  # e.g. $ 150.000
    fecha_registro: date  # revise

#################base de datos################################


database_records = Dict[int, RecordInDB]
database_records = {
    1: RecordInDB(**{"id": 1,
                     "categoria": "salary",
                     "tipo": "income",
                     "cantidad": 3000000,
                     "fecha_registro": datetime(2018, 12, 19).date()
                     }),
    2: RecordInDB(**{"id": 2,
                     "categoria": "groceries",
                     "tipo": "expense",
                     "cantidad": 150000,
                     "fecha_registro": datetime(2018, 12, 23).date()
                     }),
    3: RecordInDB(**{"id": 3,
                     "categoria": "healthcare",
                     "tipo": "expense",
                     "cantidad": 45000,
                     "fecha_registro": datetime(2018, 12, 19).date()
                     }),

    4: RecordInDB(**{"id": 4,
                     "categoria": "pet grooming",
                     "tipo": "expense",
                     "cantidad": 500000,
                     "fecha_registro": datetime(2018, 12, 25).date()
                     }),

    5: RecordInDB(**{"id": 5,
                     "categoria": "mortage",
                     "tipo": "expense",
                     "cantidad": 150000,
                     "fecha_registro": datetime(2018, 12, 26).date()
                     }),
}


##############métodos para el POST y el GET###################
generator = {"id":5}  # AUTOINCREMENTAL

def save_record(record_in_db: RecordInDB):  # CREATE RECORD (POST)
    generator["id"] = generator["id"] + 1
    record_in_db.id = generator["id"]
    database_records[record_in_db.id] = record_in_db
    return record_in_db

def get_record(id: int):  # READ RECORD (GET)
    if id in database_records.keys():
        return database_records[id]
    else:
        return None
