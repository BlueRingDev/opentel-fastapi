from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
import requests

app = FastAPI()


@app.get("/")
async def root():
    message = requests.get("http://localhost:8081/").json()
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()