FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./Database .
COPY ./API .

EXPOSE 5000

CMD ["python3", "-u", "appwithdatabase.py"]
