# Required Libraries are
import asyncio
from tabnanny import verbose
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient, Connection
from langgraph.prebuilt import create_react_agent
from typing import cast
from dotenv import load_dotenv
import os

# Importing .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key is not None:
    os.environ["GROQ_API_KEY"] = groq_api_key

# Main Function For Calling the MCP Servers
async def main():
    """
    MCP Client method: used for calling the mcp_servers
    """

    print('Called')
    
    # MCP Client
    connections: dict[str, Connection] = {
        "math_mcp_server": cast(
            Connection,
            {
            "command" : "python",
            "args" : ["/Users/mac/Documents/Learning/mcp/own_mcp_server/mcp_servers/math_mcp_server.py"],
            "transport" : "stdio",
            }
        ),
        "weather_mcp_server": cast(
            Connection,
            {
            "url" : "http://127.0.0.1:8000/mcp",
            "transport" : "streamable_http",
            }
        )    
    } 
    mcp_client = MultiServerMCPClient(connections=connections)

    # Getting Available tools from the MCP Client
    tools = await mcp_client.get_tools()
    print("Tools loaded:", [tool.name for tool in tools])


    #LLM
    llm = ChatGroq(
        model='qwen-qwq-32b'
    )

    # MCP Agent - Responsible for calling the llm and mcp_servers.
    agent = create_react_agent(
        tools=tools,
        model=llm,
        debug=True
    )

    # Checking for math_mcp_server
    #math_response = await agent.ainvoke(
    #    {"messages": [{"role": "user", "content": "what's (1 + 2) x 3?"}]}
    #)
    #print("Math MCP Server Response:", math_response['messages'][-1].content)

    # Checking for weather_mcp_server
    weather_response = await agent.ainvoke(
        {"messages":[{"role" : "user", "content" : "what is the weather in peshawar?"}]}
    )
    print('Weather MCP Server Response:', weather_response['messages'][-1].content)


# Running the main function
asyncio.run(main())

