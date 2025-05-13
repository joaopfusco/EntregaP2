from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema
from typing import List
from app.schemas.postagem_schema import PostagemOut
from app.schemas.seguidor_schema import SeguidorOut

class ParticipanteIn(BaseModel):
    ultima_notificao: str | None = None
    usuario_id: int
    evento_id: int

class ParticipanteOut(EntitySchema, ParticipanteIn):
    pass