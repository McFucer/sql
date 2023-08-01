from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import Session_local
from models import MsgModel
from schemas import MsgSchema

def get_db():
    try:
        db = Session_local()
        yield db
    finally:
        db.close()


app = FastAPI()

@app.get('/hello')
async def hello(name:str):
    return name

@app.put('/update/msg')
async def create_msg(id:int, schema: MsgSchema,
                     db:Session = Depends(get_db)):

    model = db.query(MsgModel).filter(MsgModel.id == id).first()

    if model is None:
        return 'is none'



    model.id = schema.id
    model.msg = schema.msg

    db.add(model)
    db.commit()

    return model

@app.get('/get')
async def get_msg(db: Session = Depends(get_db)):
    query = db.query(MsgModel).all()
    return query