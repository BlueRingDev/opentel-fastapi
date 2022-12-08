from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from starlette.requests import Request

app = FastAPI()

tracer = trace.get_tracer(__name__)

@app.get("/")
async def root(request: Request):
    with tracer.start_as_current_span("app-2-root") as span:
        span.set_attribute("app-2-key", "value")
        print(request.headers)
        raise Exception("app-2-root exception")
        return {"message": "Hello World From App 2"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()
