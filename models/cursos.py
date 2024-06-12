#Guilherme Saad Botrel 12121ECP018

from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from .database import Base
from typing import List
from .disciplinas import Disciplinas

class Cursos(Base):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_curso = Column(String(50), nullable=False)
    periodos = Column(Integer, nullable=False)
    faculdade = Column(String(40), nullable=False)
    id_disciplina = Column(Integer, ForeignKey('disciplinas.id'))
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))