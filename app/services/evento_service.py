from app.models.evento import Evento
from app.services.base_service import BaseService

class EventoService(BaseService):
    def __init__(self):
        super().__init__(Evento)
