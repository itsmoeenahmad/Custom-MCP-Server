"""
Weather MCP Server which will call the weather api and check the weather.
"""

# Required Libraries are
from mcp.server.fastmcp import FastMCP
import requests


# Defining the Weatehr MCP Server
weather_mcp_server = FastMCP("weather_mcp_server")


# Tool
@weather_mcp_server.tool()
def check_weather(location):
    """
    Call the weather api and get the response.
    """

    api_url = f"https://your_deployed_url/weather/{location}"

    # Calling the weather api
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data.get("result")
    except Exception as e:
        return f"Error fetching weather: {e}"


# Running the weather mcp server
if __name__ == "__main__":
    weather_mcp_server.run(transport='streamable-http')    
