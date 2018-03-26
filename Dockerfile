#Dockerfile 
#image base
FROM python:alpine

#directory di lavoro
WORKDIR /app
COPY requirements.txt /app

#dipendenze
RUN pip install -r requirements.txt
COPY . /app

#ENTRYPOINT python /app/flask_app.py
CMD [ "python", "/app/flask_app.py" ]
