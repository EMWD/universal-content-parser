import requests
from bs4 import BeautifulSoup
import config


class Parser():
    def __init__(self):
        pass

    def form_soup(self, page):
        return BeautifulSoup(page.text, 'html.parser')

    def get_page(self, page):
        return requests.get(
            url=page,
            headers={'user-agent': config.DEFAULT_HEADERS},
        )

    def get_content_by_tag_class(self, page, tag_name, tag_class):
        soup = self.form_soup(page)
        return soup.find_all(tag_name, {"class": tag_class})


parser = Parser()
