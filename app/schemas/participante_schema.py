from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema
from typing import List
from app.schemas.postagem_schema import PostagemOut
from app.schemas.seguidor_schema import SeguidorOut

class ParticipanteIn(BaseModel):
    usuario_id: int
    evento_id: int

class ParticipanteOut(EntitySchema, ParticipanteIn):
    ultima_notificao: str