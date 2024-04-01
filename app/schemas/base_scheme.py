from pydantic import BaseModel, Extra


class Base(BaseModel):
    class Config:
        from_attributes = True
        extra = Extra.forbid
