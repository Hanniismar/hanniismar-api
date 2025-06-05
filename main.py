from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "¡La API de Hanniismar está viva y lista para ti! 💖"}
