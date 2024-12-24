# Import the necessary tools from tools.py
from tools import directory_read_tool, file_read_tool, serper_search_tool, website_search_tool, retrieval_augmented_generation_tool, web_scraping_tool, my_custom_tool

def test_directory_read_tool():
    # Instantiate the DirectoryReadTool
    directory_tool = directory_read_tool
    # Test with a sample directory path
    result = directory_tool.run("sample_directory")
    print(f"Directory Read Tool Output: {result}")

def test_file_read_tool():
    # Instantiate the FileReadTool
    file_tool = file_read_tool
    # Test with a sample file path (you need to make sure this file exists in your directory)
    result = file_tool.run("sample_file.txt")
    print(f"File Read Tool Output: {result}")

def test_serper_search_tool():
    # Instantiate the SerperSearchTool
    search_tool = serper_search_tool
    # Test with a sample search query (ensure API_KEY is set in the .env file)
    result = search_tool.run("AI trends")
    print(f"Serper Search Tool Output: {result}")

def test_website_search_tool():
    # Instantiate the WebsiteSearchTool
    website_tool = website_search_tool
    # Test with a sample URL
    result = website_tool.run("https://www.example.com")
    print(f"Website Search Tool Output: {result}")

def test_retrieval_augmented_generation_tool():
    # Instantiate the RetrievalAugmentedGenerationTool
    rag_tool = retrieval_augmented_generation_tool
    # Test with a sample query and context
    result = rag_tool.run("AI trends", "Content strategy for 2024")
    print(f"Retrieval-Augmented Generation Tool Output: {result}")

def test_web_scraping_tool():
    # Instantiate the WebScrapingTool
    scraping_tool = web_scraping_tool
    # Test with a sample URL
    result = scraping_tool.run("https://www.example.com")
    print(f"Web Scraping Tool Output: {result}")

def test_my_custom_tool():
    # Instantiate the MyCustomTool
    custom_tool = my_custom_tool
    # Test with a sample product list
    result = custom_tool.run(["Product 1", "Product 2", "Product 3"])
    print(f"My Custom Tool Output: {result}")

# Run all tests
if __name__ == "__main__":
    test_directory_read_tool()
    test_file_read_tool()
    test_serper_search_tool()
    test_website_search_tool()
    test_retrieval_augmented_generation_tool()
    test_web_scraping_tool()
    test_my_custom_tool()
