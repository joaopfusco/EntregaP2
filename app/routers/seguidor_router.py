from app.db.database import get_db
from app.models.seguidor import Seguidor
from app.schemas.seguidor_schema import SeguidorOut, SeguidorIn
from app.routers.base_router import BaseRouter
from app.services.seguidor_service import SeguidorService

class SeguidorRouter(BaseRouter):
    pass

seguidor_router = SeguidorRouter(
    service=SeguidorService(),
    schema=SeguidorOut,
    create_schema=SeguidorIn,
    update_schema=SeguidorIn,
    model=Seguidor,
    db=get_db,
    prefix="/seguidores",
    tags=["Seguidores"],
)

