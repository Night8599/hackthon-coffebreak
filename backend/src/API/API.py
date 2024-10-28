from fastapi import FastAPI
from pydantic import BaseModel

from typing import Union

from csv_interfece import csvInterface_reserveTool
from csv_interfece import csvInterface_checkAvailability
from csv_interfece import csvInterface_releaseTool
from csv_searchWithAI import csvInterface_searchToolAI

import IA
app = FastAPI()

#Constantes e caminhos
nome_pasta = '../Nuvem/'

class Order(BaseModel):
    maquina: str
    problema: str

class Product(BaseModel):
    maquina: str # Frontend - input
    problema: str # Frontend - input
    manual: str # Frontend - link
    manual_resumido: str # Frontend - texto
    lista_ferramentas: str # Banco de dados

order = Order(maquina="maquina", problema="problema")
product = Product(maquina="maquina", problema="problema", manual="manual", manual_resumido="manual_resumido", lista_ferramentas="lista_ferramentas")



@app.get("/ok")
async def ok():
    return {"message": "ok"}


@app.get("/order/{maquina}/{problema}")
async def place_order(maquina: str, problema: str):
    order.maquina = maquina
    order.problema = problema
    product.maquina = maquina
    product.problema = problema

    product.manual = IA.generate_manual(nome_pasta, order.maquina)["content"]

    product.manual_resumido = IA.generate_resume(nome_pasta, product.manual, order.problema)["content"]

    product.lista_ferramentas = IA.generate_tool_list(nome_pasta, product.manual, order.problema)["content"]

    text = csvInterface_searchToolAI(product.lista_ferramentas)

    return {"produto manual": product.manual, "produto manual resumido": product.manual_resumido, "Lista de ferramentas": product.lista_ferramentas, "Lista de ferramentas com IA": text}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/searchTools/{name_tool}")
async def search_tool(name_tool: str):
    text = csvInterface_searchToolAI(product.lista_ferramentas)
    return {"message": text}

@app.get("/verify/{sap}/{start_time}/{end_time}")
async def verify_tool(sap: str, start_time: int, end_time: int):
    text = "Ferramenta não está disponível"
    if (csvInterface_checkAvailability(sap, start_time, end_time)):
        text = "Ferramenta está disponível"

    return {"message": text}

@app.get("/reserve/{sap}/{start_time}/{end_time}")
async def reserve_tool(sap: str, start_time: int, end_time: int):
    if (csvInterface_reserveTool(sap, start_time, end_time)):
        return {"message": "Tool reserved successfully"}
    else:
        return {"message": "Tool not available"}
    
@app.get("/release/{sap}/{start_time}/{end_time}")
async def release_tool(sap: str, start_time: int, end_time: int):
    if (csvInterface_releaseTool(sap, start_time, end_time)):
        return {"message": "Tool released successfully"}
    else:
        return {"message": "Tool not released"}