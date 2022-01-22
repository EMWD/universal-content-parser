from UrlFormer import uf
from Parser import parser
import config


pages = uf.get_all_pages('https://intuit.ru/studies/courses/532/388/lecture/', 9011, 2)
subpages = uf.get_all_subpages(pages, 'page', 1)

with open(config.DATA_FILE_PATH, "w") as file:
    for subpage in subpages:
        page = parser.get_page(subpage)
        res_text = parser.get_content_by_tag_class(page=page, tag_name='div', tag_class='eoi spelling-content-entity').text
        file.write(res_text)
