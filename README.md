## OpenTelemetry

### Requisitos

- [Docker](https://docs.docker.com/engine/install/)
- [Docker-compose](https://docs.docker.com/compose/install/standalone/)

### Executando 

Execute o seguinte comando no diretório raiz do projeto:

```shell
docker-compose up -d  
```

### Step by Step

- [Instrumentação sem código](instrumentação-manual.md)
- [Instrumentação com código](instrumentação-código.md)

### Explorando dados

Acesse o console do Grafana Web para explorar as métricas, traces e logs. 

- http://localhost:3000/


### Referências

[Observabilidade e Monitoramento](https://dev.to/ezziomoreira/observabilidade-e-monitoramento-1p1a)

[Três Pilares da Observabilidade](https://dev.to/ezziomoreira/tres-pilares-da-observabilidade-1p6d)

[Conceitos OpenTelemetry](https://dev.to/ezziomoreira/conceitos-opentelemetry-9k0)

[OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)

[OpenTelemetry Collector Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib)

[Visualização Gráfica das Configurações do Collector](https://www.otelbin.io/)

### Representação Gráfica das configurações do Collector

![Imagem Collector](./img/collector.png)
