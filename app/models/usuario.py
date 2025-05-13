from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.entity import Entity

class Usuario(Entity):
    nome = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    curso = Column(String, index=True, nullable=False)

    seguidores = relationship("Seguidor", foreign_keys='Seguidor.seguido_id', back_populates="seguido")
    seguindo = relationship("Seguidor", foreign_keys='Seguidor.segue_id', back_populates="segue")
    postagens = relationship("Postagem", back_populates="autor")
