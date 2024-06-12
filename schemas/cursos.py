#Guilherme Saad Botrel 12121ECP018
from pydantic import BaseModel


class Curso(BaseModel):
    id: int
    nome_curso: str
    periodos: int
    faculdade: str
    id_disciplina: int
   


    



    