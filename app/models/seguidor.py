from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from app.models.entity import Entity

class Seguidor(Entity):
    segue_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    segue = relationship("Usuario", foreign_keys=[segue_id], back_populates="seguindo")

    seguido_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    seguido = relationship("Usuario", foreign_keys=[seguido_id], back_populates="seguidores")

    __table_args__ = (
        UniqueConstraint('segue_id', 'seguido_id', name='uq_seguidor_segue_seguido'),
    )
