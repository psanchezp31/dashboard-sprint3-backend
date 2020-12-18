from db.record_db import RecordInDB
from db.record_db import save_record, get_record, get_records
from models.record_models import RecordIn, RecordOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins=[
    "http://localhost.tiangolo.com","https://localhost.tiangolo.com",
    "http://localhost","http://localhost:8080", "https://maney-app-front.herokuapp.com/",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


@api.post("/record")
async def create_record(record_in: RecordIn):
    record_in_db = RecordInDB(**record_in.dict())
    record_in_db = save_record(record_in_db)
    record_out = RecordOut(**record_in_db.dict())
    return record_out

@api.get("/record/{id}")
async def get_balance(id: int):
    record_in_db = get_record(id)
    if record_in_db == None:
        raise HTTPException(status_code=404, detail="El registro no existe")
    record_out = RecordOut(**record_in_db.dict())
    record_out.fecha_registro = record_in_db.fecha_registro.strftime("%Y-%m-%d")
    return record_out

@api.get("/records")
async def get_all_records():
    results = []
    records = get_records()
    for record in records.values():
        result = RecordOut(**record.dict())
        result.fecha_registro = record.fecha_registro.strftime("%Y-%m-%d")
        results.append(result)
    return results
