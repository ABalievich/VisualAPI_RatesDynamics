from matplotlib import pyplot as plt

from _get_info import get_rates

# cоздание вызовов API и сохранение ответов в переменных
url_usd = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=2017-1-1&endDate=2017-12-31'
url_eur = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/292?startDate=2017-1-1&endDate=2017-12-31'
url_gbp = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/143?startDate=2017-1-1&endDate=2017-12-31'

dates, rates_usd = get_rates(url_usd)
dates, rates_eur = get_rates(url_eur)
dates, rates_gbp = get_rates(url_gbp)

# нанесение данных на диаграмму
fig = plt.figure(dpi=100, figsize=(10, 6))
plt.plot(dates, rates_usd, c='green', alpha=0.5)
plt.plot(dates, rates_eur, c='red', alpha=0.5)
plt.plot(dates, rates_gbp, c='blue', alpha=0.5)

# форматирование диаграммы
title = 'Курс валют по отношению к белорускому рублю\n2017'
plt.title(title, fontsize=18)
plt.xlabel('Дата', fontsize=14)
fig.autofmt_xdate()  # выводит метки дат по диагонали
plt.ylabel('Стоимость валюты', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

# назначение диапазона для каждой оси
plt.axis([dates[0], dates[-1], 1.8, 2.8])

# сохранение диаграммы и ее вывод
plt.savefig('cur_dynamics.png')
plt.show()
