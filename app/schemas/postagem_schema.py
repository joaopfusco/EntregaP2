from datetime import datetime
from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema

class PostagemIn(BaseModel):
    autor_id: int
    evento_id: int
    conteudo: str
    data_hora: datetime
    curtidas: int
    comentarios: int

class PostagemOut(EntitySchema, PostagemIn):
    pass