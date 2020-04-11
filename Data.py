from bs4 import BeautifulSoup
import requests


def worldwide():
    source = requests.get('https://www.worldometers.info/coronavirus/').text
    soup = BeautifulSoup(source, 'lxml')
    divs = soup.find_all('div', {'class': 'maincounter-number'})
    worldwide_stat = []
    for div in divs:
        span = div.span.string
        worldwide_stat.append(span)
    return worldwide_stat



def get_country_info(url):
    source = requests.get(f'https://www.worldometers.info/coronavirus/{url}').text
    soup = BeautifulSoup(source, 'lxml')
    divs = soup.find_all('div', {'class': 'maincounter-number'})
    country_stat = []
    for div in divs:
        span = div.span.string
        country_stat.append(span)
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

def get_country_chart():
    source = requests.get('https://www.worldometers.info/coronavirus/country/us/').text
    soup = BeautifulSoup(source, 'lxml')
    divs = soup.find_all('g', {'class': 'highcharts-grid highcharts-xaxis-grid'})
    for div in divs:
        print(div)


get_country_chart()
