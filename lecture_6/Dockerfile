FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY book_api ./book_api

EXPOSE 8000

CMD ["uvicorn", "book_api.main:app", "--host", "0.0.0.0", "--port", "8000"]