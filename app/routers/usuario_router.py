from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioOut, UsuarioIn
from app.routers.base_router import BaseRouter
from app.services.usuario_service import UsuarioService

class UsuarioRouter(BaseRouter):
    pass

usuario_router = UsuarioRouter(
    service=UsuarioService(),
    schema=UsuarioOut,
    create_schema=UsuarioIn,
    update_schema=UsuarioIn,
    model=Usuario,
    db=get_db,
    prefix="/usuarios",
    tags=["Usuarios"],
)

