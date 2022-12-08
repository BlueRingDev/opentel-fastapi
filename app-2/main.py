from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World From App 2"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()
