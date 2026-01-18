import requests #type: ignore
from bs4 import BeautifulSoup #type: ignore


class WebScraper:
    def __init__(self, url: str):
        self.url = url
        self.html = None
        self.soup = None

    def fetch(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(self.url, headers=headers, timeout=10)
        response.raise_for_status()
        self.html = response.text
        self.soup = BeautifulSoup(self.html, "html.parser")

    def get_tags_with_classes(self):
        tags = {}

        for element in self.soup.find_all(True):
            tag = element.name
            classes = element.get("class", [])

            if tag not in tags:
                tags[tag] = set()

            for cls in classes:
                tags[tag].add(cls)

        # Convert sets → lists for JSON
        return {k: sorted(list(v)) for k, v in tags.items()}

    def extract(self, tag, class_name=None):
        if class_name:
            elements = self.soup.find_all(tag, class_=class_name)
        else:
            elements = self.soup.find_all(tag)

        return [el.get_text(strip=True) for el in elements]
