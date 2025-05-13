from app.models.postagem import Postagem
from app.services.base_service import BaseService
# from rabbitmq.publisher import Publisher

class PostagemService(BaseService):
    def __init__(self):
        super().__init__(Postagem)

    def create(self, data, session):
        result = super().create(data, session)
        # Publisher().publish(data.id)
        return result
