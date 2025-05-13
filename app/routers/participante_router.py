from app.db.database import get_db
from app.models.participante import Participante
from app.schemas.participante_schema import ParticipanteOut, ParticipanteIn
from app.routers.base_router import BaseRouter
from app.services.participante_service import ParticipanteService

class ParticipanteRouter(BaseRouter):
    pass

participante_router = ParticipanteRouter(
    service=ParticipanteService(),
    schema=ParticipanteOut,
    create_schema=ParticipanteIn,
    update_schema=ParticipanteIn,
    model=Participante,
    db=get_db,
    prefix="/participantes",
    tags=["Participantes"],
)
