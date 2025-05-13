from pydantic import BaseModel
from app.schemas.entity_schema import EntitySchema
from app.schemas.usuario_schema import UsuarioOut

class ParticipanteIn(BaseModel):
    ultima_notificao: str | None = None
    usuario_id: int
    evento_id: int

class ParticipanteOut(EntitySchema, ParticipanteIn):
    usuario: UsuarioOut = None