import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()

    def crawl(self):
        pages = []
        to_visit = [self.base_url]

        while to_visit:
            url = to_visit.pop(0)
            if url not in self.visited:
                self.visited.add(url)
                page = self.fetch_page(url)
                if page:
                    pages.append(page)
                    new_links = self.extract_links(page)
                    logger.info(f"Found {len(new_links)} new links on {url}")
                    to_visit.extend(new_links)

        logger.info(f"Crawling completed. Visited {len(self.visited)} pages.")
        return pages

    def fetch_page(self, url):
        try:
            logger.info(f"Fetching page: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return {'url': url, 'content': response.text}
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None

    def extract_links(self, page):
        soup = BeautifulSoup(page['content'], 'html.parser')
        links = []
        for a in soup.find_all('a', href=True):
            link = urljoin(self.base_url, a['href'])
            if link.startswith(self.base_url) and link not in self.visited:
                links.append(link)
        return links