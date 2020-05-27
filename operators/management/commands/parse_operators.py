import requests
import datetime
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from operators.models import (
    Operator,
    Organization,
)


class Operators:

    def __init__(self, name):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36 ',
            'Accept-Language': 'ru',
        }
        self.name = name

    def get_html(self):
        url = f'https://rainbowsix.fandom.com/wiki/{self.name}'
        request = self.session.get(url)
        request.raise_for_status()
        return request.text

    def get_param(self, source):
        soup = BeautifulSoup(self.get_html(), 'lxml')
        aside = soup.find('aside', class_='portable-infobox pi-background pi-europa pi-theme-wikia pi-layout-default')
        param = aside.find('div', attrs={'data-source': source}).find('div').text
        return param.strip()

    def get_stats(self):
        soup = BeautifulSoup(self.get_html(), 'lxml')
        aside = soup.find('aside', class_='portable-infobox pi-background pi-europa pi-theme-wikia pi-layout-default')
        armor = aside.find('section').find('tbody').find('tr').find_all('td')[0].find('small').text.strip()
        speed = aside.find('section').find('tbody').find('tr').find_all('td')[1].find('small').text.strip()
        return armor, speed

    def get_unique_ability(self):
        soup = BeautifulSoup(self.get_html(), 'lxml')
        ability = soup.find('table', class_='article-table') \
            .find_all('tr')[4] \
            .find_all('td')[1] \
            .find('span').text
        return ability

    def get_data(self):
        real_name = self.get_param('realname')
        organizations = self.get_param('organization').split('Rainbow')[-1].strip()
        position = self.get_param('position')
        birthplace = self.get_param('birthplace')
        date_of_birth = self.get_param('dob')
        age = self.get_param('age')
        weight = self.get_param('weight')
        height = self.get_param('height')
        armor, speed = self.get_stats()
        unique_ability = self.get_unique_ability()
        op = Operator.objects.create(
            name=self.name,
            real_name=real_name,
            position=position,
            birthplace=birthplace,
            age=age,
            weight=weight,
            height=height,
            date_of_birth=date_of_birth,
            armor_rating=armor,
            speed_rating=speed,
            unique_ability=unique_ability,
        )
        try:
            org = Organization.objects.get(name__iexact=organizations)
            org.operators.add(op)
        except:
            print(f'error - {op}')

    def run(self):
        self.get_data()


class Command(BaseCommand):
    help = 'Operators parsing'

    def handle(self, *args, **options):
        names = ['Oryx', 'Iana', 'Wamai', 'Kali', 'Amaru', 'Goyo', 'Nøkk', 'Warden', 'Mozzie', 'Gridlock', 'Nomad',
                 'Kaid',
                 'Clash', 'Maverick', 'Maestro', 'Alibi', 'Lion', 'Finka', 'Mira', 'Jackal', 'Hibana', 'Echo',
                 'Caveira',
                 'Capitão', 'Blackbeard', 'Valkyrie', 'Buck', 'Frost', 'Mute', 'Sledge', 'Smoke', 'Thatcher', 'Ash',
                 'Castle',
                 'Pulse', 'Thermite', 'Montagne', 'Twitch', 'Doc', 'Rook', 'Jäger', 'Bandit', 'Blitz', 'IQ', 'Fuze',
                 'Glaz',
                 'Tachanka', 'Kapkan']
        for name in names:
            operators = Operators(name)
            operators.run()
        self.stdout.write('parsing complete')
