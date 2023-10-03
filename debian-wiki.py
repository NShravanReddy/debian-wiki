import requests
from bs4 import BeautifulSoup

# URL of the Debian Wiki News page
url = "https://wiki.debian.org/News"

# Send an HTTP GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the content section (usually inside a <div> with id="content")
    content_div = soup.find('div', {'id': 'content'})

    if content_div:
        # Extract the text content from the HTML
        content_text = content_div.get_text()

        # Define the Markdown file name
        markdown_file_name = "debian_news.md"

        # Write the content to a Markdown file
        with open(markdown_file_name, "w", encoding="utf-8") as markdown_file:
            markdown_file.write(content_text)

        print(f"Successfully scraped and saved the Debian News to {markdown_file_name}")
    else:
        print("Error: Couldn't find the content section on the page.")
else:
    print(f"Error: Failed to fetch the page (Status code {response.status_code}).")

