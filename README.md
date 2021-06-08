# Serverless REST API

Este ejemplo demuestra cómo configurar un [Servicios Web RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services) que le permite crear, listar, obtener, actualizar y borrar listas de Tareas pendientes(ToDo). DynamoDB se utiliza para persistir los datos.

Este ejemplo está obtenido del [repositorio de ejemplo de la práctica 1](https://github.com/rgaleanog/todo-list-serverless.git) de Serverless Framework.

## Requisitos previas

- Serverless: Crear cuenta en la web de [serverless](https://app.serverless.com/).
- Github: Una cuenta personal para guardar el repositorio y generar una [nueva clave SSH](https://docs.github.com/es/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) y agregarla al ssh-agent

```bash
# settear remote git al tener la clave ssh 
git remote set-url origin git@github.com:iacutetres/todo-list-serveless.git
```
- Python3.8: Intalar python version 3.8
```bash
sudo yum install gcc openssl-devel bzip2-devel libffi-devel
cd /opt
sudo wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
sudo tar xzf Python-3.8.2.tgz
cd Python-3.8.2
sudo ./configure --enable-optimizations
sudo make altinstall
```

- todos: en este directorio se almacena el código fuente de las funciones lambda con las que se va a trabajar

## Casos de uso

- API for a Web Application
- API for a Mobile Application

## Configuración

```bash
npm install -g serverless@2.18
```

**Importante:** revisar la guía para instalar la correcta versión de serverless para evitar fallos con el login de Serverless Framework

## Despliegue con Serverless Framework

De cara a simplificar el despliegue, simplemente habría que ejecutar

```bash
serverless deploy
```

Los resultados esperados deberían de ser así:

```bash
Serverless: Packaging service…
Serverless: Uploading CloudFormation file to S3…
Serverless: Uploading service .zip file to S3…
Serverless: Updating Stack…
Serverless: Checking Stack update progress…
Serverless: Stack update finished…

Service Information
service: api-rest
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  PUT - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  DELETE - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
functions:
  api-rest-dev-update: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-update
  sapi-rest-dev-get: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-get
  api-rest-dev-list: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-list
  api-rest-dev-create: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-create
  api-rest-dev-delete: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-delete
```

## Integración con servicio CI/CD Serverless Framework

Para integrar con serverless, necesitamos loguearnos 

```bash
# serverless or sls
sls login
```
El problema venía en la versión 2.41.1 del Framework de Serverless, que no logueaba y se quedaba con:
```bash
Serverless: Logging you in via your default browser...
```
Adjunto PDF de como loguearse con serverless con SERVERLESS-ACCESS-KEY
```bash
export SERVERLESS_ACCESS_KEY=*******oMSi63F5zkLvSS2rXrVhg04*****
```

En la version 2.41.2, al ejecutar sls loguin no sale lo siguiente:
```bash
Serverless: Logging you in via your default browser...
Serverless: If your browser does not open automatically, please open the URL: https://app.serverless.com?client=cli&transactionId=*****************
```
y accediendo a la url nos loguea para poder integrarnos.
