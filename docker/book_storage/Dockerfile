FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install wait-for-it && apt-get clean

COPY book_storage/requirements.txt .
RUN pip install -r requirements.txt

COPY book_storage book_storage
COPY lib lib
COPY entrypoint.py entrypoint.py

ENV PYTHONPATH=/app
ENV DB_ADDR=db:5432
CMD wait-for-it $DB_ADDR -s -t 10 -- python /app/entrypoint.py
