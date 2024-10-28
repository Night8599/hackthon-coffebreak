# Projeto Fábrica - Gerenciamento de Ferramentas e Reservas

Este projeto é uma API desenvolvida com FastAPI para gerenciar ferramentas e suas reservas em uma fábrica. A API permite listar ferramentas, consultar reservas por código SAP e gerenciar essas informações usando um banco de dados SQLite.

## Funcionalidades

- Listar todas as ferramentas disponíveis.
- Consultar a disponibilidade e reservas de ferramentas por código SAP.

## Estrutura de Diretórios

- `app/`: Contém a aplicação principal.
- `data/`: Contém arquivos de dados (CSV) para inicializar o banco de dados.
- `tests/`: Testes automatizados.
- `.env`: Arquivo de variáveis de ambiente (opcional).

## Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-repositorio/projeto-fabrica.git
cd projeto-fabrica
