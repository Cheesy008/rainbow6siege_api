import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from operators.models import Organization


class OrganizationsParser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36 ',
            'Accept-Language': 'ru',
        }

    def get_html(self):
        url = 'https://rainbowsix.fandom.com/wiki/Rainbow'
        request = self.session.get(url)
        request.raise_for_status()
        return request.text

    @staticmethod
    def get_data(html):
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find_all('table')[1]
        tds = table.find('tr').find_all('td', attrs={"style": "width:15em;"})
        for td in tds:
            li = td.find('ul').find_all('li')
            for name in li:
                res = name.find_all('a')[1].text
                Organization.objects.create(name=res)
                print(f'Organization - {res}')

    def run(self):
        html = self.get_html()
        self.get_data(html)


class Command(BaseCommand):
    help = 'Organizations parsing'

    def handle(self, *args, **options):
        parser = OrganizationsParser()
        parser.run()
        self.stdout.write('parsing complete')
