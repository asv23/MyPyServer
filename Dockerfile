FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

COPY . .

ARG APP_PORT=8000
ENV APP_PORT=$APP_PORT
ENV PYTHONPATH=/app

EXPOSE $APP_PORT

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $APP_PORT"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]