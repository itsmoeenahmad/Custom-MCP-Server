"""
Math MCP Server which will do addition and subtraction of a two numbers.
"""

# Required Libraies are
from mcp.server.fastmcp import FastMCP


# Defining the Math MCP Server
math_mcp_server = FastMCP("math_mcp_server")

# Tool # 01
@math_mcp_server.tool()
def add(a:int, b:int)-> int:
    """
    Add two numbers
    """
    return a+b

# Tool # 02
@math_mcp_server.tool()
def subbtract(a:int, b:int)-> int:
    """
    Subtract two numbers
    """
    return a-b

# Tool # 03
@math_mcp_server.tool()
def multiply(a:int, b:int)-> int:
    """
    Multiply two numbers
    """
    return a*b

# Tool # 04
@math_mcp_server.tool()
def divide(a:int, b:int)-> float:
    """
    Divide two numbers
    """
    return a/b

# For Running the math mcp server
if __name__ == "__main__":
    math_mcp_server.run(transport='stdio') 