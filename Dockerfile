
FROM python:3.8-slim-buster
COPY . /app/
WORKDIR /app

RUN pip3 install -r requirements.txt

ENV FLASK_SECRET_KEY="OVD8q3vaXLYFoPBJiDg45E0xQHqnnVJW"

EXPOSE 8080
CMD ["./run.sh"]

