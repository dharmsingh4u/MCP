from mcp.server import MCPServer

mcp = MCPServer("Math") ## this is server name.

@mcp.tool()
def add(a: int, b:int)->int:
    """this is for adding two numbers"""
    return a+b
@mcp.tool()
def multiply(a: int, b:int)->int:
    """this is for multiply two numbers"""
    return a*b

app = mcp.streamable_http_app(
    streamable_http_path="/mcp",
    json_response=True,
    stateless_http=True,
    host="0.0.0.0",
)
