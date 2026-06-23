from fastapi import FastAPI

app = FastAPI()

#endpoint de inicio
@app.get("/")
def inicio():
    return {"message": "Hola estoy aprendiendo FASTAPI"}