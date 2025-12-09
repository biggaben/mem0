FROM python:3.12-slim

LABEL org.opencontainers.image.name="mem0/openmemory-mcp"

WORKDIR /usr/src/openmemory

# Install system dependencies and Doppler CLI
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg && \
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | gpg --dearmor -o /usr/share/keyrings/doppler-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/doppler-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list && \
    apt-get update && apt-get install -y doppler && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY config.json .
COPY . .

EXPOSE 8765
CMD ["doppler", "run", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765"]
