#Guilherme Saad Botrel 12121ECP018
from fastapi import FastAPI
from typing import Optional
from routers.cursos import router as router_cursos
from routers.disciplinas import router as router_disciplnas
from models.database import engine
from models.cursos import Cursos
from models.disciplinas import Disciplinas
from models.cursos import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_cursos)
app.include_router(router_disciplnas)

