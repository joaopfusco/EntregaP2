from app.models.postagem import Postagem
from app.services.base_service import BaseService

class PostagemService(BaseService):
    def __init__(self):
        super().__init__(Postagem)
