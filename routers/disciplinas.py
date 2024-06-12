#Guilherme Saad 12121ECP018

from fastapi import APIRouter, Depends, HTTPException, Response, status
from schemas.disciplinas import Disciplina
from models.database  import get_db
from models.disciplinas    import Disciplinas
from sqlalchemy.orm   import Session

router = APIRouter()

@router.get("/disciplinas")
async def root():
    return {"mensagem": "Dentro de disciplinas"}

@router.post("/disciplinas")
async def criar_disciplina(disciplina: Disciplina, db: Session = Depends(get_db)):
    nova_disciplina = Disciplinas(**disciplina.model_dump())
    db.add(nova_disciplina)
    db.commit()
    db.refresh(nova_disciplina)
    return { "mensagem": "Disciplina criado com sucesso",
             "disciplina": nova_disciplina 
    }

@router.delete("/disciplinas/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Disciplinas).filter(Disciplinas.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Disciplina não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/disciplina/{id}")
def update(id: int, aluno:Disciplina, db:Session = Depends(get_db)):
    updated_post = db.query(Disciplinas).filter(Disciplinas.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Disciplina: {id} does not exist')
    else:
        updated_post.update(aluno.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()
    