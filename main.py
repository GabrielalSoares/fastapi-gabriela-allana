from fastapi import FastAPI

app = FastAPI(title='API de Gabriela e Allana')

@app.get("/")
def hello():
     return{"message": "Hello World!"}

@app.get("/aluno")
def get_aluno():
     return{"insira a rota após a '/' o nome do aluno"}

@app.get("/aluno/{nome_aluno}")
def get_aluno_by_name(nome_aluno:str):
     return{"o nome do aluno é": nome_aluno}