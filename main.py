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
    bdd.append(usuario)
    return {"mensaje": f"el usuario fue agregado {usuario}"}

@app.get("/usuarios")
def mostrar_usuario():
    return bdd

@app.delete("/usuario/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    for usuario in bdd:
        if usuario["id"] == usuario_id:
            bdd.remove(usuario)
            return {"message": "el usuario a sido eliminado"}
        
    return {"message": "el usuario no ha sido encontrado"}

@app.put("/user/{usuario_id}")
def modificar_usuario(usuario_id: int, usuario_actualizado: Usuario):
    for usuario in bdd:
        if usuario.id == usuario_id:
            usuario.name = usuario_actualizado.name
            return {"message": "el usuario ha sido actualizado"}
        
    return {"message": "el usuario no ha sido encontrado"}
