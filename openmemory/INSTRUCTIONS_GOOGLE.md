# How to run OpenMemory with Google Gemini and Doppler

I have modified the OpenMemory backend to support Google Gemini models and integrated Doppler for secret management.

## Changes Made

1. **Modified `api/app/utils/memory.py`**: Added logic to check `LLM_PROVIDER` and `EMBEDDER_PROVIDER` environment variables (defaults to `gemini-3-pro-preview`).
2. **Updated `api/requirements.txt`**: Added `google-genai` library support.
3. **Updated `api/Dockerfile`**: Installed Doppler CLI and configured it as the entrypoint.
4. **Updated `docker-compose.yml`**: Added `DOPPLER_TOKEN` support and updated run command.

## Setup Instructions

### 1. Configure Doppler

1. Create a Project and Config in [Doppler](https://dashboard.doppler.com).
2. Add the following secrets to your Doppler config:

    ```code
    GOOGLE_API_KEY=your_google_api_key_here
    LLM_PROVIDER=gemini
    # Default is gemini-3-pro-preview, but you can be explicit:
    LLM_MODEL=gemini-3-pro-preview
    
    EMBEDDER_PROVIDER=gemini
    EMBEDDER_MODEL=models/gemini-embedding-001
    # gemini-embedding-001 defaults to 3072 dimensions
    EMBEDDING_DIMS=3072
    
    USER=default_user
    ```

3. Generate a Service Token for your config.

### 2. Run with Docker

You need to provide the `DOPPLER_TOKEN` to the container.

**First, rebuild the container:**

```bash
cd openmemory
docker-compose up --build
```

**Run using the token:**

```bash
# You can set the token in your shell or pass it inline
export DOPPLER_TOKEN=dp.st.your_service_token
docker-compose up
```

### 3. Verify

Watch the logs. You should see "Using LLM provider: gemini".
The Doppler CLI will automatically inject the secrets from your project into the application environment.

## Local Development (No Docker)

To run locally, you need the [Doppler CLI installed](https://docs.doppler.com/docs/install-cli).

1. Login and select your project:

    ```bash
    doppler login
    doppler setup
    ```

2. Run the application with `doppler run`:

    ```bash
    cd openmemory/api
    doppler run -- uvicorn main:app --host 0.0.0.0 --port 8765
    ```
