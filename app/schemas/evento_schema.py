from datetime import datetime
from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema
from typing import List
from app.schemas.participante_schema import ParticipanteOut

class EventoIn(BaseModel):
    nome: str
    local: str
    descricao: str
    data_hora: datetime
    inscritos: int
    aberto: bool

class EventoOut(EntitySchema, EventoIn):
    participantes: List[ParticipanteOut] = []
