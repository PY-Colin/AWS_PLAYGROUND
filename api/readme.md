### Python + FastAPI + Mangum + AWS Lambda Container

A demo project to test the AWS Lambda container support with Python FastAPI framework. The purpose of the project is to show how to develop a REST API with FastAPI, how to build & test it locally and how to deploy it on AWS using serverless services (AWS ECR, AWS Lambda & AWS API Gateway).

### Prerequisites

- Docker CLI
- Python 3.10

### Install dependencies

A requirements file declare all dependencies (Mangum, FastAPI, Uvicorn, ...). Use the following command to install the required dependencies (For Python 3.10)

```
pip install -r ./requirements.txt
```

TIP : Before installing required dependencies, do not forget to create a virtual environment.

### Run locally

You can either use the following command :

```
python -m app.app
```

Or deploy on uvicorn :

```
uvicorn app.app:app --reload --host 0.0.0.0 --port 5000
```

You can test the application by using the following command : 

```
curl http://localhost:5000/event/
```

### Build the 'regular' container

This command builds a container which will run a Uvicorn server and deploy the ASGI app on it : 

```
docker build -t epole-world . 
```

### Run the container

The command starts the container :

```
docker run -p 5000:5000 epole-world:latest
```

You can make a test with this command :

```
curl http://localhost:5000/event/
```
