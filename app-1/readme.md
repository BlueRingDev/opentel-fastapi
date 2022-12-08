Following instructions from https://app.aspecto.io/

# Dependencies
poetry add opentelemetry-instrumentation
poetry add opentelemetry-distro
poetry add opentelemetry-exporter-otlp-proto-grpc

Running `opentelemetry-bootstrap --action=requirements` outputs these requirements

poetry add opentelemetry-instrumentation-aws-lambda
poetry add opentelemetry-instrumentation-dbapi
poetry add opentelemetry-instrumentation-logging
poetry add opentelemetry-instrumentation-sqlite3
poetry add opentelemetry-instrumentation-urllib
poetry add opentelemetry-instrumentation-wsgi
poetry add opentelemetry-instrumentation-fastapi
poetry add opentelemetry-instrumentation-grpc
poetry add opentelemetry-instrumentation-requests
poetry add opentelemetry-instrumentation-urllib3  


# Environment variables
OTEL_SERVICE_NAME=<your-service-name> \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://otelcol.aspecto.io:4317 \
OTEL_EXPORTER_OTLP_HEADERS=Authorization=e230367b-fdbb-4c55-b120-41e95f012486 \

# Running app
opentelemetry-instrument uvicorn main:app --reload --port 8080
