from pydantic import BaseModel, Field, ValidationError


class ObjData(BaseModel):
    year: int
    price: int
    CPU_model: str = Field(alias='CPU model')


class ObjectWithData(BaseModel):
    name: str
    data: ObjData
