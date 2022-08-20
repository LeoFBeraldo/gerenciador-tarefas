from fastapi import FastAPI

app = FastAPI()

TAREFAS = TAREFAS = [
    {
        "id": "1",
        "titulo": "estudar programação",
        "descrição": "bootcamp de python",
        "estado": "não finalizado",
    },
    {
        "id": "2",
        "titulo": "levar o cachorro para passear",
        "descrição": "está muito sujo",
        "estado": "não finalizado",
    },
    {
        "id": "3",
        "titulo": "lavar roupas",
        "descrição": "estão sujas",
        "estado": "não finalizado",
    },
]


@app.get("/tarefas")
def listar():
    return TAREFAS
