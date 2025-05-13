from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema
from typing import List
from app.schemas.seguidor_schema import SeguidorOut

class UsuarioIn(BaseModel):
    nome: str
    email: str
    curso: str
    telefone: str

class UsuarioOut(EntitySchema, UsuarioIn):
    seguidores: List[SeguidorOut] = []
    seguindo: List[SeguidorOut] = []