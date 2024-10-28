from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .crud import get_ferramentas, get_reservas_by_codigo_sap

router = APIRouter()

@router.get("/ferramentas/")
def listar_ferramentas(db: Session = Depends(get_db)):
    return get_ferramentas(db)

@router.get("/reservas/{codigo_sap}")
def listar_reservas(codigo_sap: str, db: Session = Depends(get_db)):
    return get_reservas_by_codigo_sap(db, codigo_sap)
