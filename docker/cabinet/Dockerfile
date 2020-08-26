FROM python:3.8

WORKDIR /app

COPY cabinet/requirements.txt .
RUN pip install -r requirements.txt

COPY cabinet cabinet
COPY lib lib
COPY entrypoint.py entrypoint.py

ENV PYTHONPATH=/app
CMD python /app/entrypoint.py
