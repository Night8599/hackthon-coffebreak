import openai
import os

# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

def ler_nome_arquivo_na_pasta(nome_pasta): # Pasta contendo os arquivos dos manuais das maquinas
    arquivos = os.listdir(nome_pasta)
    return arquivos

def generate_manual(nome_pasta, machine):
    manuais = ler_nome_arquivo_na_pasta(nome_pasta)
    messages = [
        {
            "role": "user",
            "content": f"""Visando solucionar um problema de uma maquina {machine}, procure o manual da maquina na lista abaixo e retorne apenas o nome do arquivo: {manuais}"""
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    return response.choices[0].message

def generate_resume(nome_pasta, nome_manual, problem):
    with open(f"{nome_pasta}/{nome_manual}", "r") as file:
        manual = file.read()

    messages = [
        {
            "role": "user",
            "content": f"""Elabore uma solução passo a passo baseada no manual considerando o problema {problem}. Manual: {manual}"""
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message

def generate_tool_list(nome_pasta, nome_manual, problem):
    with open(f"{nome_pasta}/{nome_manual}", "r") as file:
        manual = file.read()
    messages = [
        {
            "role": "user",
            "content": f"""Gostaria de uma lista de ferramentas necessárias para seguir o manual considerando o problema {problem}. O formato da lista deve ser as ferramentas separadas por quebra de linha. O manual é o seguinte: {manual}"""
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message

