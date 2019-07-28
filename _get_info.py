import requests
from datetime import datetime


def get_rates(url):
    # сохранение ответа API в переменной
    resp_url = requests.get(url)
    dynamics = resp_url.json()

    # чтение дат и официального курса валюты
    dates, rates = [], []
    for dynamic in dynamics:
        date = datetime.strptime(dynamic['Date'], "%Y-%m-%dT%H:%M:%S")
        rate = dynamic['Cur_OfficialRate']

        dates.append(date)
        rates.append(rate)

    return dates, rates
