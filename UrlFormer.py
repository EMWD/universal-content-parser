import requests


class UrlFormer():
    def __init__(self):
        pass

    def check_url_exists(self, url: str):
        ''' Если сайт редиректит, считаем, что нужной страницы нет'''
        return requests.head(url, allow_redirects=False).status_code == 200

    def get_all_pages(self, page_url: str, init_number: int, step: int):
        ''' Пример: page_url='https://intuit.ru/studies/courses/532/388/lecture/' and init_number=9001 '''

        if type(init_number) != int:
            init_number = int(init_number)

        valid_pages = []
        while self.check_url_exists(page_url + str(init_number)):
            valid_pages.append(page_url + str(init_number))
            init_number += step

        return valid_pages

    def get_all_subpages(self, pages: dict, param='page', init_number=1):

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
