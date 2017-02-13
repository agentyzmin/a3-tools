import copy

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
import pandas as pd
import locale

EXCHANGE_TIME = 180
# TODO: change to 'uk_UA.utf8' before deploying to heroku // local -> 'Ukrainian_Ukraine.1252'
LOCALE = 'Ukrainian_Ukraine.1252'
line_files = ['redline.csv', 'blueline.csv', 'greenline.csv']
MAP_SQUARES = {'Akademmistechko': 'A1', 'Arsenalna': 'C2', 'Beresteiska': 'A2', 'Boryspilska': 'C3',
               'Chernihivska': 'C2', 'Chervonyi Khutir': 'C3', 'Darnytsia': 'C2', 'Demiivska': 'B3', 'Dnipro': 'C2',
               'Dorohozhychi': 'B1', 'Druzhby Narodiv': 'B3', 'Heroiv Dnipra': 'B1', 'Hidropark': 'C2',
               'Holosiivska': 'B3', 'Ipodrom': 'A3', 'Kharkivska': 'C3', 'Khreschatyk': 'B2', 'Klovska': 'B2',
               'Kontraktova Ploscha': 'B2', 'Lisova': 'C2', 'Livoberezhna': 'C2', 'Lukianivska': 'B2', 'Lybidska': 'B3',
               'Maidan Nezalezhnosti': 'B2', 'Minska': 'B1', 'Nyvky': 'A1', 'Obolon': 'B1', 'Olimpiiska': 'B2',
               'Osokorky': 'C3', 'Palats Sportu': 'B2', 'Palats Ukraina': 'B3', 'Pecherska': 'B3', 'Petrivka': 'B1',
               'Ploscha Lva Tolstoho': 'B2', 'Politekhnichnyi Instytut': 'A2', 'Poshtova Ploscha': 'B2',
               'Pozniaky': 'C3', 'Shuliavska': 'A2', 'Slavutych': 'B3', 'Sviatoshyn': 'A1', 'Syrets': 'B1',
               'Tarasa Shevchenka': 'B1', 'Teatralna': 'B2', 'Teremky': 'A3', 'Universytet': 'B2', 'Vasylkivska': 'B3',
               'Vokzalna': 'B2', 'Vydubychi': 'B3', 'Vyrlytsia': 'C3', 'Vystavkovyi Tsentr': 'B3', 'Zhytomyrska': 'A1',
               'Zoloti vorota': 'B2'}


def set_ukr_locale():
    try:
        locale.setlocale(locale.LC_ALL, 'uk_UA.utf8')
    except:
        locale.setlocale(locale.LC_ALL, 'Ukrainian_Ukraine.1252')


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
            'Palats Ukraina': 'Палац «Україна»', 'Pecherska': 'Печерська', 'Petrivka': 'Петрівка',
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


def get_line_stations():
    kyiv_lines = []
    module_dir = os.path.dirname(__file__)  # get current directory
    for line_file in line_files:
        file_path = os.path.join(module_dir, 'static/metrolines/' + line_file)
        with open(file_path) as infile:
            kyiv_lines.append(pd.read_csv(infile, dtype=object))

    result = {}
    for index, line in enumerate(kyiv_lines):
        for station in list(line.columns)[1:]:
            result[station] = 'M' + str(index + 1)
    return result


# Create your views here.
def get_metrotimer(request):
    set_ukr_locale()
    stations = get_all_stations_ukr()
    context = {
        'stationsUK': sorted(stations.values(), key=locale.strxfrm),
        'stationsEN': sorted(stations.keys())
    }
    return render(request, 'metrotimer.html', context)


@csrf_exempt
def post_metrotimer(request):
    rounding = bool(request.POST['rounding'])
    print(rounding)
    origin_station = request.POST['station']
    times_en = get_all_times(origin_station)
    times_ua = dict()
    set_ukr_locale()
    stations_ua = get_all_stations_ukr()
    line_stations = get_line_stations()
    for key in times_en:
        if rounding:
            times_en[key] = (times_en[key] // 300 + (1 if times_en[key] % 300 > 0 else 0)) * 300
        times_en[key] = {
            'time': str(int(times_en[key] / 60)) + '.' + format(times_en[key] % 60, '02d'),
            'station': key,
            'line': line_stations[key],
            'map_square': MAP_SQUARES[key]
        }
        times_ua[stations_ua[key]] = copy.copy(times_en[key])
        times_ua[stations_ua[key]]['station'] = stations_ua[key]

    print(sorted(times_en.items()))

    response = JsonResponse({'times_en': sorted(times_en.items()),
                             'times_ua': sorted(times_ua.items(), key=lambda x: locale.strxfrm(x[0]))})

    return response
