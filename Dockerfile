FROM python:3.9-slim

WORKDIR /app

COPY . /app

EXPOSE 5000

RUN pip install -r quirements.txt
CMD ["python", "app.py"]