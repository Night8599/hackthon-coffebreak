from sqlalchemy.orm import Session
from . import models

# Função para obter todas as ferramentas
def get_ferramentas(db: Session):
    return db.query(models.Ferramenta).all()

# Função para obter as reservas de uma ferramenta específica
def get_reservas_by_codigo_sap(db: Session, codigo_sap: str):
    return db.query(models.Reserva).filter(models.Reserva.codigo_sap == codigo_sap).all()
