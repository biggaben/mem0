import os
import sys
from dotenv import load_dotenv

# Ensure the 'api' directory is in the Python path so 'app' module can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Load environment variables from .env file directly (before imports)
from dotenv import load_dotenv
env_path = os.path.join(current_dir, ".env")
load_dotenv(env_path)

# Import the FastMCP instance
# Note: This import works because we added current_dir to sys.path
from app.mcp_server import mcp

if __name__ == "__main__":
    # Run the MCP server with stdio transport logic
    # FastMCP.run() defaults to stdio if no transport is specified, 
    # but we can be explicit.
    mcp.run(transport='stdio')
    
    # Run the MCP server with stdio transport logic
    # FastMCP.run() defaults to stdio if no transport is specified, 
    # but we can be explicit.
    mcp.run(transport='stdio')
