FROM python:3.9-slim-buster

WORKDIR /root

COPY . /root

RUN pip install -r requirements.txt

RUN chmod +x ./start.sh

EXPOSE 3000

CMD . ./env.sh && python3 app.py