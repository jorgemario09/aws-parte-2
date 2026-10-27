# Workshop CRUD de TODOs con AWS SAM · Python

API REST Serverless construida con AWS Serverless Application Model (SAM), Amazon API Gateway, AWS Lambda, Amazon DynamoDB, Amazon SNS y Amazon SQS.

## ¿Qué aprendimos?
- Despliegue de arquitecturas orientadas a eventos utilizando **SNS** como publicador y **SQS** como consumidor con filtros de eventos (`FilterPolicy`).
- Manejo de reintentos resilientes mediante **Dead Letter Queues (DLQ)** y procesamiento de fallos en lotes (`ReportBatchItemFailures`).
- Persistencia e historial de auditoría desacoplado utilizando claves de ordenamiento (`sk`) en DynamoDB.

## Reto adicional resuelto
- Implementación del endpoint de historial (`/todos/{id}/history`) utilizando consultas eficientes (`Query`) sobre la tabla de auditoría con `KeyConditionExpression` para recuperar toda la traza evolutiva de cada tarea.