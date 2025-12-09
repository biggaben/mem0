# OpenMemory

OpenMemory is your personal memory layer for LLMs - private, portable, and open-source. Your memories live locally, giving you complete control over your data. Build AI applications with personalized memories while keeping your data secure.

![OpenMemory](https://github.com/user-attachments/assets/3c701757-ad82-4afa-bfbe-e049c2b4320b)

## Easy Setup

### Prerequisites
- Docker
- Google Gemini API Key

You can quickly run OpenMemory by running the following command:

**Linux/macOS:**
```bash
curl -sL https://raw.githubusercontent.com/mem0ai/mem0/main/openmemory/run.sh | bash
```

**Windows (PowerShell):**
```powershell
iwr -useb https://raw.githubusercontent.com/mem0ai/mem0/main/openmemory/run.ps1 | iex
```

You should set the `GOOGLE_API_KEY` as a global environment variable:

**Linux/macOS:**
```bash
export GOOGLE_API_KEY=your_api_key
```

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_api_key"
```

You can also set the `GOOGLE_API_KEY` as a parameter to the script:

**Linux/macOS:**
```bash
curl -sL https://raw.githubusercontent.com/biggaben/mem0/main/openmemory/run.sh | GOOGLE_API_KEY=your_api_key bash
```

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_api_key"; iwr -useb https://raw.githubusercontent.com/biggaben/mem0/main/openmemory/run.ps1 | iex
```

## Prerequisites

- Docker and Docker Compose
- Python 3.9+ (for backend development)
- Node.js (for frontend development)
- Google Gemini API Key

## Quickstart

### 1. Set Up Environment Variables

Before running the project, you need to configure environment variables.

#### Option A: Using `run.sh` (Quickest)

You can run the project directly with environment variables.

**For Linux/macOS:**


```bash
# For Google Gemini
export GOOGLE_API_KEY=your_api_key
export LLM_PROVIDER=gemini
./run.sh
```

**For Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_api_key"
$env:LLM_PROVIDER="gemini"
.\run.ps1
```

#### Option B: Manual Docker Compose

Create a `.env` file in `api/`:

```env
# api/.env
LLM_PROVIDER=gemini
GOOGLE_API_KEY=your_gemini_key
USER=default_user
```

Then run:
```bash
make build
make up
```

#### UI Configuration
The UI connects to the backend at `http://localhost:8765`. If you need to change this, check `ui/.env.example`.

### 2. Build and Run the Project
You can run the project using the following two commands:
```bash
make build # builds the mcp server and ui
make up  # runs openmemory mcp server and ui
```

After running these commands, you will have:
- OpenMemory MCP server running at: http://localhost:8765 (API documentation available at http://localhost:8765/docs)
- OpenMemory UI running at: http://localhost:3000

#### UI not working on `localhost:3000`?

If the UI does not start properly on [http://localhost:3000](http://localhost:3000), try running it manually:

```bash
cd ui
pnpm install
pnpm dev
```

### MCP Client Setup

Use the following one step command to configure OpenMemory Local MCP to a client. The general command format is as follows:

```bash
npx @openmemory/install local http://localhost:8765/mcp/<client-name>/sse/<user-id> --client <client-name>
```

Example:
```bash
npx @openmemory/install local http://localhost:8765/mcp/antigravity/sse/default_user --client antigravity
```

Replace `<client-name>` with the desired client name and `<user-id>` with the value specified in your environment variables.

### Local MCP via Stdio (Claude Desktop)

To use OpenMemory with Claude Desktop or other Stdio MCP clients:

1.  Ensure you have `uv` installed.
2.  Add the configuration to your MCP client config (e.g. `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "openmemory": {
      "command": "uv",
      "args": [
        "run",
        "api/run_mcp.py"
      ],
      "cwd": "/absolute/path/to/openmemory",
      "env": {
        "GOOGLE_API_KEY": "AIza...",
        "LLM_PROVIDER": "gemini",
        "EMBEDDER_PROVIDER": "gemini",
        "USER_ID": "default_user",
        "MCP_CLIENT_NAME": "default_client"
      }
    }
  }
}
```

> [!NOTE]
> The database services (Postgres, Qdrant) must be running (e.g., via `docker-compose up mem0_store`).



## Project Structure

- `api/` - Backend APIs + MCP server
- `ui/` - Frontend React application

## Contributing

We are a team of developers passionate about the future of AI and open-source software. With years of experience in both fields, we believe in the power of community-driven development and are excited to build tools that make AI more accessible and personalized.

We welcome all forms of contributions:
- Bug reports and feature requests
- Documentation improvements
- Code contributions
- Testing and feedback
- Community support

How to contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b openmemory/feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin openmemory/feature/amazing-feature`)
5. Open a Pull Request

Join us in building the future of AI memory management! Your contributions help make OpenMemory better for everyone.
