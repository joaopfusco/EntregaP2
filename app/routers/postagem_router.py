from app.db.database import get_db
from app.models.postagem import Postagem
from app.schemas.postagem_schema import PostagemOut, PostagemIn
from app.routers.base_router import BaseRouter
from app.services.postagem_service import PostagemService

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
