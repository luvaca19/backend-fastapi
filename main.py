from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#creamos el modelo de datos, en este caso un usuario

class Usuario(BaseModel):
    id: int
    name: str

bdd = []

@app.post("/usuario")
def crear_usuario(usuario: Usuario):
    bdd.append(usuario.dict())
    return {"mensaje": f"el usuario fue agregado {usuario}"}

@app.get("/usuarios")
def mostrar_usuario():
    return bdd


