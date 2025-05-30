from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.entity import Entity

class Participante(Entity):
    ultima_notificacao = Column(String, index=True, nullable=True)

    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    usuario = relationship("Usuario", backref="participantes")

    evento_id = Column(Integer, ForeignKey('evento.id'), nullable=False)
    evento = relationship("Evento", back_populates="participantes")
