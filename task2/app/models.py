from typing import List

from pydantic import BaseModel


class CatModel(BaseModel):
    age: int
    name: str
    features: List[str]


class DBError(Exception):
    pass
