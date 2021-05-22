from requests import Session
import json

coins = ['BTC', 'ETH', 'LTC', 'ADA', 'BNB', 'DOT']

#  for each coin in the coins array, add price to price array
def get_price_data():
    result_arr = []

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

        result_arr.append("{:.2f}".format(json.loads(
                        response.text)
                        ['data'][coin]['quote']['USD']['price']))

    print(result_arr)

    return result_arr
