from app.models.postagem import Postagem
from app.services.base_service import BaseService
from rabbitmq.publisher import publish

class PostagemService(BaseService):
    def __init__(self):
        super().__init__(Postagem)

    def create(self, data, session):
        result = super().create(data, session)
        publish(result.id)
        return result
