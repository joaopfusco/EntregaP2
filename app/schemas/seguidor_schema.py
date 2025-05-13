from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema

class SeguidorIn(BaseModel):
    segue_id: int
    seguido_id: int

class SeguidorOut(EntitySchema, SeguidorIn):
    pass