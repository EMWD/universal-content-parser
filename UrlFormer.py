import requests
from icecream import ic


class UrlFormer():
    def __init__(self):
        pass

    def check_url_exists(self, url: str):
        ''' Если сайт редиректит, считаем, что нужной страницы нет'''
        return requests.head(url, allow_redirects=False).status_code == 200

    def get_pages(self, page_url: str, init_number: int, search_range: int=None, step: int=None):
        ''' 
        Пример: page_url='https://intuit.ru/studies/courses/532/388/lecture/' and init_number=9001 
        Метод начинает искать станицы либо по номеру с указанным шагом, либо по номеру с указанным диапазоном  
        '''

        valid_pages = []
        if type(init_number) != int:
            init_number = int(init_number)

        if step:
            while self.check_url_exists(page_url + str(init_number)):
                valid_pages.append(page_url + str(init_number))
                init_number += step
        elif search_range:
            range_count = 0
            for _ in range(search_range):
                formed_url = page_url + str(init_number + range_count)
                if self.check_url_exists(formed_url):
                    valid_pages.append(formed_url)
                range_count += 1
        else:
            raise ValueError('Not enough params for search')

        return valid_pages

    def get_subpages(self, pages: dict, param='page', init_number: int=1):

        if pages:
            if type(init_number) != int:
                init_number = int(init_number)

            valid_subpages = []
            for page_url in pages:
                if page_url[-1] != '/':
                    page_url += '/'

                while self.check_url_exists(f'{page_url}?{param}={init_number}'):
                    valid_subpages.append(f'{page_url}?{param}={init_number}')
                    init_number += 1
                init_number = 1
            return valid_subpages

        raise(ValueError('Have no pages'))


uf = UrlFormer()
