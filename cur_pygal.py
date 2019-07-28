import pygal

from _get_info import get_rates

# cоздание вызовов API и сохранение ответов в переменных
url_usd = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=2018-8-1&endDate=2018-8-31'
url_eur = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/292?startDate=2018-8-1&endDate=2018-8-31'
url_gbp = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/143?startDate=2018-8-1&endDate=2018-8-31'

dates, rates_usd = get_rates(url_usd)
dates, rates_eur = get_rates(url_eur)
dates, rates_gbp = get_rates(url_gbp)

# визуализация результатов
line = pygal.Line()

line.title = 'Курс валют по отношению к белорускому рублю\nАвгуст 2018'
line.x_labels = map(lambda d: d.strftime('%d'), dates)
line.x_title = 'Число'
line.y_title = 'Стоимость валюты'

line.add('USD', rates_usd)
line.add('EUR', rates_eur)
line.add('GBP', rates_gbp)

line.render_to_file('cur_dynamics.svg')
