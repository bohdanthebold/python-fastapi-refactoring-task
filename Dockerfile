FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
