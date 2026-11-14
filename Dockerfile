FROM ghcr.io/astral-sh/uv:python3.13-alpine AS builder
WORKDIR /app

# Install the application dependencies
COPY . /app

RUN uv build

FROM python:3.13-alpine

COPY --from=builder /app/dist/*.whl /tmp/

RUN pip install /tmp/*.whl

ENTRYPOINT [ "arithmp" ]