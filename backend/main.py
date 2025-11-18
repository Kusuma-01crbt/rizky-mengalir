from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "aktif", "version": "demo-1.0"}

@app.get("/bot-status")
def bot_status():
    return {
        "bot": "running",
        "mode": "demo",
        "message": "Siap mengalirkan rezeki"
    }
