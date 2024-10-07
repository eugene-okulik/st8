from pydantic import Field, BaseModel


class ObjectDataJson(BaseModel):
    year: int or list[int]
    price: float
    CPU_model: str = Field(alias='CPU model')


class ObjectJson(BaseModel):
    name: str
    data: ObjectDataJson
