import requests


def etherscan_transactions(address):
    API_KEY = "PQWGH496A8A1H3YV5TKWNVCPHJZ3S7ITHA"

    url = "https://api.etherscan.io/api?module=account&action=txlist&address="\
          + address + \
          "&startblock=0&endblock=99999999&sort=asc&apikey=" + API_KEY
          
    response = requests.get(url)
    response_json = response.json()
    transactions = response_json.get("result")
    
    for transaction in transactions:
        print(transaction)