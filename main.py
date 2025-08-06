from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import os

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

app = FastAPI()

VERIFY_TOKEN = "mi_token_secreto"

@app.get("/webhook")
async def verify(request: Request):
    args = dict(request.query_params)
    if args.get("hub.mode") == "subscribe" and args.get("hub.verify_token") == VERIFY_TOKEN:
        return PlainTextResponse(content=args["hub.challenge"])
    return PlainTextResponse(content="Error de verificación", status_code=403)

@app.post("/webhook")
async def receive(request: Request):
    body = await request.json()
    print("📩 Mensaje recibido:", body)
    return {"status": "ok"}
