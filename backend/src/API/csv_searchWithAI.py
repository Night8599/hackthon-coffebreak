# Import openai library
import openai

# Import CSV library
import csv

import os


# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the path to the CSV files
tools_csv_path = 'tools.csv'
tools_availability_csv_path = 'tools_availability.csv'




# Implement the function to get all tools
def csvInterface_getTools() -> str:

    # Open the tools.csv file
    with open(tools_csv_path, mode='r') as tools_file:

        # Create a CSV reader object
        tools_reader = csv.reader(tools_file)

        # Convert everything to string type
        tools = list(tools_reader)

        return tools
    
# Implement the function to search tool SAP with AI
def csvInterface_searchToolAI(tools_name: str) -> str:

    # Get all tools list from the CSV file
    tools_list = csvInterface_getTools()

    messages = [

        {

            "role": 'user',
            "content": f"""Gostaria que você buscasse a SAP das ferramentas: {tools_name} na tabela: {tools_list}, quero apenas a lista de código SAP nada mais, nessa formatação: ['Ferramentas de Medição', 'Micrômetro', 'MAT102']"""

        }

    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message