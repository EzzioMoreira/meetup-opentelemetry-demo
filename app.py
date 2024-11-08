from flask import Flask
import requests
from time import sleep
import random
import logging
################################################################################
### Adicione aqui o código que importa OpenTelemetry e instancia a SDK ########
################################################################################
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.semconv.trace import SpanAttributes

provider = TracerProvider()
span_exporter = OTLPSpanExporter()
processor = BatchSpanProcessor(span_exporter)
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = Flask(__name__)
latency = random.randint(1, 5)

@app.route("/fetch-data")
def fetch_data_from_external_service():
        with tracer.start_as_current_span("fetch_data_from_external_service") as span:
            # Simula uma solicitação HTTP GET para um serviço externo
            response = requests.get("http://httpbin.org/get")
            span.set_attribute(SpanAttributes.HTTP_METHOD, "GET")
            span.set_attribute(SpanAttributes.HTTP_FLAVOR, "1.1")
            span.set_attribute(SpanAttributes.HTTP_ROUTE, "/get")
            span.set_attribute(SpanAttributes.HTTP_URL, "http://httpbin.org")
            span.set_attribute(SpanAttributes.HTTP_STATUS_CODE, response.status_code)
            span.set_attribute("I_like", "rapadura")
            span.add_event("a operação foi realizada com sucesso com:", {
                "status_code": str(response.status_code),
                "request_headers": str(response.request.headers),
            })
            sleep(latency)
            logging.info(f"GET request to httpbin.org returned {response.status_code}")
            return f"GET request to httpbin.org returned {response.status_code}"
            span.end()

@app.route("/submit-data")
def submit_data_to_external_service():
    # Simula uma solicitação HTTP POST para um serviço externo
    response = requests.post("http://httpbin.org/post", json={"key": "value"})
    sleep(latency)
    logging.info(f"POST request to httpbin.org returned {response.status_code}")
    return f"POST request to httpbin.org returned {response.status_code}"

@app.route("/simulate-error")
def simulate_error_response():
    # Simula uma solicitação HTTP que retorna um erro
    response = requests.get("http://httpbin.org/status/403")
    sleep(latency)
    logging.error(f"GET request to httpbin.org returned {response.status_code}")
    return f"GET request to httpbin.org returned {response.status_code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
