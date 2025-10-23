FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]