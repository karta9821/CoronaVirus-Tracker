from bs4 import BeautifulSoup
import requests


def get_country_info(url=''):
    source = requests.get(f'https://www.worldometers.info/coronavirus/{url}').text
    soup = BeautifulSoup(source, 'lxml')
    divs = soup.find_all('div', {'class': 'maincounter-number'})
    country_stat = []
    for div in divs:
        span = div.span.string
        country_stat.append(span)
    try:
        divs_active_cases = soup.find_all('div', {'class': 'panel_front'})
        for div in divs_active_cases:
            if div.get('class', 'number-table-main'):
                country_stat.append(div.div.text)
                country_stat.append(div.span.text)
                country_stat.append(div.strong.text)
        serious = (int(country_stat[3].replace(',', '')) - int(country_stat[4].replace(',', '')))
        serious_perc = str(100 - int(country_stat[5]))
        deaths = (int(country_stat[6].replace(',', '')) - int(country_stat[7].replace(',', '')))
        deaths_perc = str(100 - int(country_stat[8]))
        country_stat.append(f'{serious:,}')
        country_stat.append(serious_perc)
        country_stat.append(f'{deaths:,}')
        country_stat.append(deaths_perc)
    except IndexError or TypeError:
        for i in range(10):
            country_stat.append('----')
    return country_stat


def available_countries():
    source = requests.get('https://www.worldometers.info/coronavirus/').text
    soup = BeautifulSoup(source, 'lxml')
    countries = soup.find_all('a', {'class': 'mt_a'})
    dic_countries = {}
    dic_countries['Worldwide'] = ''
    for country in countries:
        dic_countries[country.string] = country.get('href')
    return dic_countries

