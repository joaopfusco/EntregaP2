from app.models.participante import Participante
from app.services.base_service import BaseService

class ParticipanteService(BaseService):
    def __init__(self):
        super().__init__(Participante)
