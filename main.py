import random
from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll n six-sided dice and return the result of each die."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def two_number(a: int, b: int) -> int:
    """Add two integers and return their sum."""
    return a + b

if __name__ == "__main__":
    mcp.run()