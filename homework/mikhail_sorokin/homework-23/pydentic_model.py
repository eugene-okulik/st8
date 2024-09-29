from pydantic import BaseModel, Field


class ObjectDataJson(BaseModel):
    year: str
    price: float or int
    cpu_nodel: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class ObjectJson(BaseModel):
    name: str
    data: ObjectDataJson
