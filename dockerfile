FROM ubuntu:24.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | \
    env UV_UNMANAGED_INSTALL="/usr/local/bin" sh

COPY . .

RUN uv sync --locked --no-dev

CMD ["uv", "run", "--no-sync", "fastapi", "run", "src/main.py"]