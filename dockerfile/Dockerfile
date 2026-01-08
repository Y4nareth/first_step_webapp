FROM python:3.10-alpine

LABEL VERSION="0.2.1"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./dockerfile/entrypoint.sh
RUN chmod +x /usr/local/bin/daphne || true

ENTRYPOINT [ "./dockerfile/entrypoint.sh" ]