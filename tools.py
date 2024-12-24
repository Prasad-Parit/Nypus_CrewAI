from crewai.tools import DirectoryReadTool
from crewai.tools import FileReadTool
from crewai.tools import SerperDevTool
from crewai.tools import WebsiteSearchTool
from langchain.agents import tool

# Directory Read Tool
@tool
def directory_read_tool(directory_path: str):
    """Reads and lists files from the specified directory."""
    return DirectoryReadTool.read(directory_path)

# File Read Tool
@tool
def file_read_tool(file_path: str):
    """Reads content from a specified file."""
    return FileReadTool.read(file_path)

# Serper Search Tool
@tool
def serper_search_tool(query: str):
    """Searches the web using Serper."""
    return SerperDevTool.search(query)

# Website Search Tool
@tool
def website_search_tool(website_url: str, query: str):
    """Searches for information on a specific website."""
    return WebsiteSearchTool.search(website_url, query)

# Custom Tool (Example)
@tool
def my_custom_tool(param1: str, param2: str):
    """Performs a custom function tailored to the team's needs."""
    # Replace with your custom functionality.
    return f"Custom functionality executed with {param1} and {param2}."
