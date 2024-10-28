from fastapi import FastAPI
from .database import engine
from .models import Base
from .api import router

# Inicializa o FastAPI
app = FastAPI()

# Cria as tabelas no banco de dados (caso não existam)
Base.metadata.create_all(bind=engine)

# Registra as rotas da API
app.include_router(router)
