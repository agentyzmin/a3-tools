# coding=utf-8
import os

import pandas as pd
from django.contrib.staticfiles.templatetags.staticfiles import static

EXCHANGE_TIME = 300


def get_all_stations_list():
    return ['Akademmistechko', 'Arsenalna', 'Beresteiska', 'Boryspilska', 'Chernihivska', 'Chervonyi Khutir',
            'Darnytsia', 'Demiivska', 'Dnipro', 'Dorohozhychi', 'Druzhby Narodiv', 'Heroiv Dnipra', 'Hidropark',
            'Holosiivska', 'Ipodrom', 'Kharkivska', 'Khreschatyk', 'Klovska', 'Kontraktova Ploscha', 'Lisova',
            'Livoberezhna', 'Lukianivska', 'Lybidska', 'Maidan Nezalezhnosti', 'Minska', 'Nyvky', 'Obolon',
            'Olimpiiska', 'Osokorky', 'Palats Sportu', 'Palats Ukraina', 'Pecherska', 'Petrivka',
            'Ploscha Lva Tolstoho', 'Politekhnichnyi Instytut', 'Poshtova Ploscha', 'Pozniaky', 'Shuliavska',
            'Slavutych', 'Sviatoshyn', 'Syrets', 'Tarasa Shevchenka', 'Teatralna', 'Teremky', 'Universytet',
            'Vasylkivska', 'Vokzalna', 'Vydubychi', 'Vyrlytsia', 'Vystavkovyi Tsentr', 'Zhytomyrska', 'Zoloti vorota']


def get_all_stations_ukr():
    return {'Akademmistechko': "Академмістечко", 'Arsenalna': 'Арсенальна', 'Beresteiska': 'Берестейська',
            'Boryspilska': 'Бориспільська', 'Chernihivska': 'Чернігівська', 'Chervonyi Khutir': 'Червоний хутір',
            'Darnytsia': 'Дарниця', 'Demiivska': 'Деміївська', 'Dnipro': 'Дніпро', 'Dorohozhychi': 'Дорогожичі',
            'Druzhby Narodiv': 'Дружби народів', 'Heroiv Dnipra': 'Героїв Дніпра', 'Hidropark': 'Гідропарк',
            'Holosiivska': 'Голосіївська', 'Ipodrom': 'Іподром', 'Kharkivska': 'Харківська', 'Khreschatyk': 'Хрещатик',
            'Klovska': 'Кловська', 'Kontraktova Ploscha': 'Контрактова площа', 'Lisova': 'Лісова',
            'Livoberezhna': 'Лівобережна', 'Lukianivska': 'Лук\'янівська', 'Lybidska': 'Либідська',
            'Maidan Nezalezhnosti': 'Майдан Незалежності', 'Minska': 'Мінська', 'Nyvky': 'Нивки', 'Obolon': 'Оболонь',
            'Olimpiiska': 'Олімпійська', 'Osokorky': 'Осокорки', 'Palats Sportu': 'Палац спорту',
            'Palats Ukraina': 'Палац Україна', 'Pecherska': 'Печерська', 'Petrivka': 'Петрівка',
            'Ploscha Lva Tolstoho': 'Площа Льва Толстого', 'Politekhnichnyi Instytut': 'Політехнічний інститут',
            'Poshtova Ploscha': 'Поштова площа', 'Pozniaky': 'Позняки', 'Shuliavska': 'Шулявська',
            'Slavutych': 'Славутич', 'Sviatoshyn': 'Святошин', 'Syrets': 'Сирець',
            'Tarasa Shevchenka': 'Тараса Шевченка', 'Teatralna': 'Театральна', 'Teremky': 'Теремки',
            'Universytet': 'Університет', 'Vasylkivska': 'Васильківська', 'Vokzalna': 'Вокзальна',
            'Vydubychi': 'Видубичі', 'Vyrlytsia': 'Вирлиця', 'Vystavkovyi Tsentr': 'Виставковий центр',
            'Zhytomyrska': 'Житомирська', 'Zoloti vorota': 'Золоті ворота'}


def get_time_on_line(origin_station, line):
    result = dict()
    for index, row in line.iterrows():
        if row[0] == origin_station:
            for key in row.keys():
                try:
                    time = row[key].split('.')
                    time = int(time[0]) * 60 + int(time[1])
                    result[key] = time
                except ValueError:
                    pass
    return result


def find_line(station, lines):
    for line in lines:
        if station in line.columns:
            return line


def get_all_times(origin_station):
    line_files = ['blueline.csv', 'redline.csv', 'greenline.csv']
    kyiv_lines = []

    exchange_stations = {
        'Ploscha Lva Tolstoho': 'Palats Sportu',
        'Palats Sportu': 'Ploscha Lva Tolstoho',
        'Maidan Nezalezhnosti': 'Khreschatyk',
        'Khreschatyk': 'Maidan Nezalezhnosti',
        'Zoloti vorota': 'Teatralna',
        'Teatralna': 'Zoloti vorota'
    }

    module_dir = os.path.dirname(__file__)  # get current directory
    for line_file in line_files:
        file_path = os.path.join(module_dir, 'static/metrolines/' + line_file)
        with open(file_path) as infile:
            kyiv_lines.append(pd.read_csv(infile, dtype=object))

    origin_line = find_line(origin_station, kyiv_lines)
    result = dict()

    result.update(get_time_on_line(origin_station, origin_line))
    for line in kyiv_lines:
        if line.columns[1] != origin_line.columns[1]:
            exchanges = {}
            for key in exchange_stations:
                if key in origin_line.columns and exchange_stations[key] in line.columns:
                    exchanges[key] = exchange_stations[key]

            for exchange in exchanges:
                time_till_exchange = result[exchange]
                time_on_lines = get_time_on_line(exchanges[exchange], line)
                for key in time_on_lines:
                    total_time = time_on_lines[key] + time_till_exchange + EXCHANGE_TIME
                    if key not in result or result[key] > total_time:
                        result[key] = total_time
    return result
