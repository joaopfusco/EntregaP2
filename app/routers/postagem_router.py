from app.db.database import get_db
from app.models.postagem import Postagem
from app.schemas.postagem_schema import PostagemOut, PostagemIn
from app.routers.base_router import BaseRouter
from app.services.postagem_service import PostagemService
from rabbitmq.publisher import Publisher

class PostagemRouter(BaseRouter):
    pass

postagem_router = PostagemRouter(
    service=PostagemService(),
    schema=PostagemOut,
    create_schema=PostagemIn,
    update_schema=PostagemIn,
    model=Postagem,
    db=get_db,
    prefix="/postagens",
    tags=["Postagens"],
)

@postagem_router.get("/send_message/{postagem_id}")
def send_message(postagem_id: int):
    publisher = Publisher()
    publisher.send_message(postagem_id)
    return { "result": "Mensagem enviada!" }