from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Estado del bot (activo o no)
bot_status = {"active": False}

# Modelo para posibles configuraciones futuras
class Config(BaseModel):
    strategy: str = "SMA"  # Simple Moving Average por defecto
    capital: float = 1000

@app.get("/")
def read_root():
    return {"message": "¡Hanniismar está en línea y lista para operar!"}

@app.post("/bot/start")
def start_bot(config: Config):
    if bot_status["active"]:
        return {"status": "ya activo"}
    bot_status["active"] = True
    # Aquí iría lógica real para iniciar el bot con config
    return {"status": "iniciado", "config": config}

@app.post("/bot/stop")
def stop_bot():
    if not bot_status["active"]:
        return {"status": "ya detenido"}
    bot_status["active"] = False
    return {"status": "detenido"}

@app.get("/bot/status")
def get_status():
    return {"active": bot_status["active"]}
