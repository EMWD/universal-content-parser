from UrlFormer import uf
from Parser import parser
import config


pages = uf.get_pages('https://intuit.ru/studies/courses/532/388/lecture/', init_number=9001, search_range=None, step=2)
subpages = uf.get_subpages(pages, 'page', 1)

with open(config.DATA_FILE_PATH, "w") as file:
    for subpage in subpages:
        page = parser.get_page(subpage)
        parsed_tags = parser.get_content_by_tag_class(page=page, tag_name='div', tag_class='eoi spelling-content-entity')
        for parsed_tag in parsed_tags:
            file.write(parsed_tag.text.strip())


