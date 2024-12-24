import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is missing. Please make sure to set the API key in the .env file.")

# Tool 1: Directory Read Tool
class DirectoryReadTool:
    def __init__(self):
        self.name = "directory_read_tool"
        self.description = "Reads and processes files in a specified directory for relevant content."

    def run(self, directory_path):
        # Placeholder function for reading directory contents
        return f"Reading files from directory: {directory_path}"

# Tool 2: File Read Tool
class FileReadTool:
    def __init__(self):
        self.name = "file_read_tool"
        self.description = "Reads content from a specified file."

    def run(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return f"Content from file {file_path}: {content}"

# Tool 3: Serper Search Tool (Example for API Usage)
class SerperSearchTool:
    def __init__(self):
        self.name = "serper_search_tool"
        self.description = "Fetches trending topics and search results from the Serper API."

    def run(self, query):
        headers = {
            'Authorization': f'Bearer {API_KEY}',  
            'Content-Type': 'application/json'
        }

        # Assuming Serper API endpoint for search trends
        url = f"https://api.serper.com/v1/search?q={query}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  
            return response.json()  
        except requests.exceptions.RequestException as e:
            return f"Error fetching data from Serper API: {str(e)}"

# Tool 4: Website Search Tool (Scraping tool example)
class WebsiteSearchTool:
    def __init__(self):
        self.name = "website_search_tool"
        self.description = "Scrapes content from specified websites to gather relevant data."

    def run(self, url):
        return f"Scraping content from: {url}"

# Tool 5: Retrieval-Augmented Generation Tool
class RetrievalAugmentedGenerationTool:
    def __init__(self):
        self.name = "retrieval_augmented_generation_tool"
        self.description = "Generates content by retrieving and combining information from various sources."

    def run(self, query, context):
        return f"Generating content for query '{query}' with context '{context}'"

# Tool 6: Web Scraping Tool
class WebScrapingTool:
    def __init__(self):
        self.name = "web_scraping_tool"
        self.description = "Scrapes web pages to extract data and insights for content creation."

    def run(self, url):
        return f"Scraping web page: {url}"

# Tool 7: Custom Tool (For specific needs)
class MyCustomTool:
    def __init__(self):
        self.name = "my_custom_tool"
        self.description = "A custom tool for handling specific use cases in content creation."

    def run(self, product_list):
        return f"Generating product descriptions for: {product_list}"

# Instantiate all tools
directory_read_tool = DirectoryReadTool()
file_read_tool = FileReadTool()
serper_search_tool = SerperSearchTool()
website_search_tool = WebsiteSearchTool()
retrieval_augmented_generation_tool = RetrievalAugmentedGenerationTool()
web_scraping_tool = WebScrapingTool()
my_custom_tool = MyCustomTool()
