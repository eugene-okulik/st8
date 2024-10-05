from pydantic import BaseModel


class PublicationObject(BaseModel):
    id: int
    title: str
    body: str
    userId: int
