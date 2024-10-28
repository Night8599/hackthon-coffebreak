from sqlalchemy import Column, String, Integer, Time, Boolean
from .database import Base

# Modelo para a tabela de ferramentas
class Ferramenta(Base):
    __tablename__ = 'ferramentas'
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String)
    descricao = Column(String, nullable=False)
    codigo_sap = Column(String, unique=True, nullable=False)

# Modelo para a tabela de reservas
class Reserva(Base):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True, index=True)
    codigo_sap = Column(String, nullable=False)
    hora = Column(Time, nullable=False)
    status = Column(Boolean, nullable=False)
