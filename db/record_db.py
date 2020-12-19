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

database_records = {
    1: RecordInDB(**{"id": 1,
                     "categoria": "Salary",
                     "tipo": "Income",
                     "cantidad": 3000000,
                     "fecha_registro": datetime(2018, 12, 19).date()
                     }),
    2: RecordInDB(**{"id": 2,
                     "categoria": "Pet",
                     "tipo": "Expense",
                     "cantidad": 150000,
                     "fecha_registro": datetime(2018, 12, 23).date()
                     }),
    3: RecordInDB(**{"id": 3,
                     "categoria": "Health",
                     "tipo": "Expense",
                     "cantidad": 45000,
                     "fecha_registro": datetime(2018, 12, 19).date()
                     }),
    4: RecordInDB(**{"id": 4,
                     "categoria": "Pet",
                     "tipo": "Expense",
                     "cantidad": 500000,
                     "fecha_registro": datetime(2018, 12, 25).date()
                     }),
    5: RecordInDB(**{"id": 5,
                     "categoria": "Food",
                     "tipo": "Expense",
                     "cantidad": 150000,
                     "fecha_registro": datetime(2018, 12, 26).date()
                     }),
}


##############métodos para el POST y el GET###################
generator = {"id": 5}  # AUTOINCREMENTAL

def save_record(record_in_db: RecordInDB):  # CREATE RECORD (POST)
    new_id = generator["id"] + 1
    generator["id"] = new_id
    record_in_db.id = new_id
    database_records[new_id] = record_in_db
    return record_in_db

def get_record(id: int):  # READ RECORD (GET)
    if id in database_records.keys():
        return database_records[id]
    else:
        return None

def get_records(): 
    return database_records

def delete_record(id: int):
    delete_response = database_records.pop(id)
    return delete_response

