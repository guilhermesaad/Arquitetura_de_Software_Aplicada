#Guilherme Saad Botrel 12121ECP018

from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from .database import Base

class Disciplinas(Base):
    __tablename__ = 'disciplinas'

    id =  Column(Integer, primary_key=True, autoincrement=True)
    nome_disciplina = Column(String(50), nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    discente = Column(String(40), nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))

