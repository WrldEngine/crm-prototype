from typing import NewType

from pydantic import BaseModel, Extra

PyModel = NewType("PyModel", BaseModel)


class Base(BaseModel):
    class Config:
        from_attributes = True
        extra = Extra.forbid


class OrmSchemeModel(BaseModel):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
