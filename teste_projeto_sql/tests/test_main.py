from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Testa se a rota de listar ferramentas está funcionando corretamente
def test_listar_ferramentas():
    response = client.get("/ferramentas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Deve retornar uma lista

# Testa se a rota de listar reservas por código SAP está funcionando corretamente
def test_listar_reservas():
    codigo_sap = "MAT001"  # Ajuste conforme os dados de teste
    response = client.get(f"/reservas/{codigo_sap}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Deve retornar uma lista de reservas
