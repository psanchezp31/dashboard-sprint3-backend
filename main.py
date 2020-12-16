from db.record_db import RecordInDB
from db.record_db import save_record, get_record

from models.record_models import RecordIn, RecordOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()


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
