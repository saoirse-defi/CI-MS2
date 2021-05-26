from requests import Session
import json

coins = ['BTC', 'ETH', 'LTC', 'ADA', 'BNB', 'DOT', 'AMPL', 'XRP', 'LINK']


#  for each coin in the coins array, add price to price array
def get_price_data():
    price_dict = {}

    for coin in coins:

        URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

        parameters = {
            'symbol': coin,
            'convert': 'USD'
        }

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'aa16ac70-6d93-4398-b90e-1584fe9ce595'
        }

        session = Session()  # Browsing session, saves cookies, headers

        session.headers.update(headers)

        response = session.get(URL, params=parameters)

        price_dict[coin] = "{:.2f}".format(json.loads(
                        response.text)
                        ['data'][coin]['quote']['USD']['price'])

    return price_dict
