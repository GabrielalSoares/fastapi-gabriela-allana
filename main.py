from fastapi import FastAPI

app = FastAPI(title='API de Gabriela e Allana')

@app.get("/")
def hello():
     return{"message": "Hello World!"}