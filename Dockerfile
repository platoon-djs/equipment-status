FROM python:alpine

WORKDIR /var/www
 
RUN pip install Flask

ENTRYPOINT ["python", "main.py"] 
