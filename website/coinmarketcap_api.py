from requests import Session
import json


def get_coin_price(symbol):
    URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'aa16ac70-6d93-4398-b90e-1584fe9ce595'
    }

    session = Session()  # Browsing session, saves cookies, headers

    session.headers.update(headers)

    response = session.get(URL, params=parameters)

    return json.loads(response.text)['data'][symbol]['quote']['USD']['price']
