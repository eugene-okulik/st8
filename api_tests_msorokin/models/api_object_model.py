from pydantic import BaseModel


class ObjectDataJson(BaseModel):
    year: str
    price: float or int
    cpu_nodel: str
    hard_disk_size: str


class ObjectJson(BaseModel):
    name: str
    data: ObjectDataJson
