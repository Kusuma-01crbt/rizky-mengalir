from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "aktif", "versi": "demo-1.0"}

@app.get("/status-bot")
def status_bot():
    return {
        "bot": "berlari",
        "mode": "demo",
        "pesan": "Siap mengalirkan rezeki"
    }
