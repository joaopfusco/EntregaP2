from app.models.seguidor import Seguidor
from app.services.base_service import BaseService

class SeguidorService(BaseService):
    def __init__(self):
        super().__init__(Seguidor)

    def create(self, data, session):
        if data.seguido_id == data.segue_id:
            raise ValueError("Não é possível seguir a si mesmo.")
        return super().create(data, session)
    
    def update(self, item_id, data, session):
        if data.seguido_id == data.segue_id:
            raise ValueError("Não é possível seguir a si mesmo.")
        return super().update(item_id, data, session)