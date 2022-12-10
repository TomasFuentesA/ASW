FROM bitnami/python:3.8.13

COPY . .

RUN pip install flask
RUN pip install psycopg2-binary

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]

