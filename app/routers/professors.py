from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/professors",
    tags=["professors"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Professor)
def create_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    return crud.create_professor(db=db, professor=professor)

@router.get("/{professor_id}", response_model=schemas.Professor)
def read_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, professor_id=professor_id)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor not found")
    return db_professor

@router.delete("/{professor_id}")
def delete_professor(professor_id: int, db: Session = Depends(get_db)):
    success = crud.delete_professor(db, professor_id=professor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Professor not found")
    return {"detail": "Professor deleted successfully"}
