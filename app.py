from fastapi import FastAPI
from routes import personas, caminatas, registros

app = FastAPI()

@app.get("/")
async def root():
    return {"mensaje": "¡La API de Caminatas está funcionando!"}


app.include_router(personas.router)
app.include_router(caminatas.router)
#app.include_router(registros.router)