import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    """
    Scrapes the given web page and returns its title and all links on the page.

    Args:
        url (str): The URL of the web page to scrape.

    Returns:
        dict: A dictionary with the page title and a list of links.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get the page title
        title = soup.title.string if soup.title else 'No Title Found'

        # Find all links on the page
        links = []
        for a_tag in soup.find_all('a', href=True):
            links.append(a_tag['href'])

        return {
            'title': title,
            'links': links
        }

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    data = scrape_webpage(url)
    if data:
        print(f"Title: {data['title']}")
        print("Links found on the page:")
        for link in data['links']:
            print(link)
