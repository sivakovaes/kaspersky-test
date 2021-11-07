import json
import requests


BASE_URL = "https://min-api.cryptocompare.com/data/pricemulti?tsyms=USD&fsyms="


def request_currency_by_type(currency_type='BTC'):
    url = BASE_URL + currency_type
    res = requests.get(url)

    if res.status_code != 200:
        print("Error")

    res_data = res.json()
    cost = res_data.get(currency_type, {}).get('USD')
    return cost


def request_currency():
    url = BASE_URL + "BTC,ETH,LTC"
    res = requests.get(url)

    if res.status_code != 200:
        print("Error")

    res_data = res.json()

    currency = {
        "BTC": res_data.get('BTC', {}).get('USD'),
        "ETH": res_data.get('ETH', {}).get('USD'),
        "LTC": res_data.get('LTC', {}).get('USD')
    }
    return currency
