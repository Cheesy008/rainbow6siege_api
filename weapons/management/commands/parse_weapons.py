import os

import requests
from bs4 import BeautifulSoup
from django.conf import settings

from django.core.management.base import BaseCommand

from weapons.models import (
    Weapon,
    Attachments,
)
from operators.models import (
    Organization,
    Operator,
)


class Weapons:

    def __init__(self, weapon):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36 ',
            'Accept-Language': 'ru',
        }
        self.weapon = weapon

    def get_html(self):
        url = f'https://rainbowsix.fandom.com/wiki/{self.weapon}'
        request = self.session.get(url)
        request.raise_for_status()
        return request.text

    def get_general_info(self, data):
        weapon_name = self.weapon.replace('/Siege', ' ')
        general_section = data.find_all(
            'section',
            class_='pi-item pi-group pi-border-color'
        )[0]
        weapon_type = general_section.find(
            'div',
            attrs={'data-source': 'type'}
        ).find('div').text.strip()
        weapon_fire = general_section.find(
            'div',
            attrs={'data-source': 'fire'}
        ).find('div').text.strip()
        weapon_users = general_section.find(
            'div',
            attrs={'data-source': 'users'}
        ).find('div').find_all('a')
        weapon_affiliation = general_section.find(
            'div',
            attrs={'data-source': 'affiliation'}
        ).find('div').text.strip()
        data = {
            'weapon_name': weapon_name,
            'weapon_users': weapon_users,
            'weapon_affiliation': weapon_affiliation,
            'weapon_type': weapon_type,
            'weapon_fire': weapon_fire,
        }

        return data

    def parse_damage(self, weapon_type, html):
        if weapon_type == 'standard':
            dam1 = html.find_all('br')[0].next_sibling.strip()
            dist1 = html.find_all('small')[0].text.strip()
            dam2 = html.find_all('br')[1].next_sibling.strip()
            dist2 = html.find_all('small')[1].text.strip()
            result = f'{dam1} {dist1}, {dam2} {dist2}'
            return result
        else:
            dam1 = html.find_all('br')[3].next_sibling.strip()
            dist1 = html.find_all('small')[2].text.strip()
            dam2 = html.find_all('br')[4].next_sibling.strip()
            dist2 = html.find_all('small')[3].text.strip()
            result = f'{dam1} {dist1}, {dam2} {dist2}'
            return result

    def get_stats(self, data):
        stats_section = data.find_all(
            'section',
            class_='pi-item pi-group pi-border-color'
        )[1]
        weapon_damage_unparsed = stats_section.find(
            'div',
            attrs={'data-source': 'damage per hit'}
        ).find('div')
        weapon_standard_damage = self.parse_damage('standard', weapon_damage_unparsed)
        weapon_suppressed_damage = self.parse_damage('suppressed', weapon_damage_unparsed)
        weapon_mobility = stats_section.find(
            'div',
            attrs={'data-source': 'mobility'}
        ).find('div').text.strip()
        weapon_rate_of_fire = stats_section.find(
            'div',
            attrs={'data-source': 'rate of fire'}
        ).find('div').text.strip()
        weapon_magazine = stats_section.find(
            'div',
            attrs={'data-source': 'magazine'}
        ).find('div').text.strip()
        data = {
            'weapon_standard_damage': weapon_standard_damage,
            'weapon_suppressed_damage': weapon_suppressed_damage,
            'weapon_mobility': weapon_mobility,
            'weapon_magazine': weapon_magazine,
            'weapon_rate_of_fire': weapon_rate_of_fire,
        }
        try:
            weapon_ammotype = stats_section.find(
                'div',
                attrs={'data-source': 'ammotype'}
            ).find('div').text.strip()
        except:
            pass
        else:
            data['weapon_ammotype'] = weapon_ammotype

        return data

    def get_attachments(self, soup):
        div = soup.find('div', class_='mw-content-text')
        table = div.find('table', class_='article-table')
        data = {}
        try:
            sights = table.find_all('tr')[0].find('ul')
            data['sights'] = sights
        except:
            pass
        try:
            barrels = table.find_all('tr')[1].find('ul')
            data['barrels'] = barrels
        except:
            pass
        try:
            grips = table.find_all('tr')[2].find('ul')
            data['grips'] = grips
        except:
            pass
        try:
            under_barrels = table.find_all('tr')[3].find('ul')
            data['under_barrels'] = under_barrels
        except:
            pass

        return data

    def set_attachments(self, name, data, weapon):
        for attachment in data:
            try:
                a = Attachments.objects.get(name__iexact=attachment.text.strip())
                if name == 'sights':
                    a.sights.add(weapon)
                elif name == 'barrels':
                    a.barrels.add(weapon)
                elif name == 'grips':
                    a.grips.add(weapon)
                elif name == 'under_barrels':
                    a.under_barrels.add(weapon)
            except Attachments.DoesNotExist:
                print("Doesn't exist doesn't exist TRUTH (Attachment)")

    def get_data(self):
        soup = BeautifulSoup(self.get_html(), 'lxml')
        data_aside = soup.find(
            'aside',
            class_='portable-infobox pi-background pi-europa pi-theme-wikia pi-layout-stacked'
        )
        general_info = self.get_general_info(data_aside)
        stats = self.get_stats(data_aside)
        attachments = self.get_attachments(soup)
        try:
            affiliation = Organization.objects.get(name=general_info['weapon_affiliation'])
        except Organization.DoesNotExist:
            print("Doesn't exist doesn't exist TRUTH (Organization)")
        else:
            w = Weapon.objects.create(
                name=general_info['weapon_name'],
                type=general_info['weapon_type'],
                affiliation=affiliation,
                standard_damage=stats['weapon_standard_damage'],
                suppressed_damage=stats['weapon_suppressed_damage'],
                ammunition_type=stats.get('weapon_ammotype', 'Undefined'),
                magazine_size=stats['weapon_magazine'],
                rate_of_fire=stats['weapon_rate_of_fire'],
                mobility=int(stats['weapon_mobility'])
            )

            for user in general_info['weapon_users']:
                op = Operator.objects.get(name__iexact=user.text.strip())
                op.weapons.add(w)

            try:
                self.set_attachments('sights', attachments['sights'], w)
            except:
                pass
            try:
                self.set_attachments('barrels', attachments['barrels'], w)
            except:
                pass
            try:
                self.set_attachments('grips', attachments['grips'], w)
            except:
                pass
            try:
                self.set_attachments('under_barrels', attachments['under_barrels'], w)
            except:
                pass

    def run(self):
        self.get_data()


class Command(BaseCommand):
    help = 'Weapon parsing'

    def handle(self, *args, **options):
        path_to_file = os.path.join(settings.BASE_DIR, 'files', 'weapon_names.txt')
        with open(path_to_file, 'r', encoding='utf-8') as f:
            for name in f:
                print(name)
                weapons = Weapons(name.strip())
                weapons.run()
        self.stdout.write('parsing complete')

