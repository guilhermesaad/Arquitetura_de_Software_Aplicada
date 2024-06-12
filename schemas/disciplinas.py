#Guilherme Saad Botrel 12121ECP018
from pydantic import BaseModel


class Disciplina(BaseModel):
    id: int
    nome_disciplina: str
    carga_horaria: int
    discente: str
    