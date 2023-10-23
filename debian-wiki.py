import requests
from bs4 import BeautifulSoup
import os

# URL of the Debian Wiki News page
WIKI_URL = "https://wiki.debian.org/News"

# Function to fetch and parse the web page
def fetch_debian_news():
    try:
        # Send an HTTP GET request to the wiki page
        response = requests.get(WIKI_URL)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main content section
        content = soup.find(id='content')

        # Extract the formatted content
        formatted_content = content.prettify()

        return formatted_content
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to write the content to a Markdown file
def write_to_markdown(content):
    try:
        with open("debian_news.md", "w", encoding="utf-8") as file:
            file.write(content)
        print("Debian News has been converted to Markdown and written to debian_news.md")
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")

# Main function
def main():
    news_content = fetch_debian_news()
    if news_content:
        write_to_markdown(news_content)

if __name__ == "__main__":
    main()
