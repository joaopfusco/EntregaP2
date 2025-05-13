from app.db.database import get_db
from app.models.evento import Evento
from app.schemas.evento_schema import EventoOut, EventoIn
from app.routers.base_router import BaseRouter
from app.services.evento_service import EventoService

class EventoRouter(BaseRouter):
    pass

evento_router = EventoRouter(
    service=EventoService(),
    schema=EventoOut,
    create_schema=EventoIn,
    update_schema=EventoIn,
    model=Evento,
    db=get_db,
    prefix="/eventos",
    tags=["Eventos"],
)

