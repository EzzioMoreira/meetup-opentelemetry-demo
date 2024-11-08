#!/bin/bash

# Função para fazer requisições
make_requests() {
  endpoints=("fetch-data" "submit-data" "simulate-error")
  for endpoint in "${endpoints[@]}"; do
    url="http://localhost:8080/$endpoint"
    echo "GET $url"
    curl -X GET $url
    sleep 10
  done
}

# Loop infinito para fazer requisições a cada 30 segundos
while true; do
  make_requests
done
