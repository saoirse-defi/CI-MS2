import requests


def etherscan_transactions(API_KEY, address):
    url = "https://api.etherscan.io/api?module=account&action=txlist&address="\
            + address + \
            "&startblock=0&endblock=99999999&sort=asc&apikey=" + API_KEY
    response = requests.get(url)
    response_json = response.json()
    transactions = response_json.get("result")
    
    for transaction in transactions:
        print(transaction)


etherscan_transactions("PQWGH496A8A1H3YV5TKWNVCPHJZ3S7ITHA", 
                       "0x2158bC4E35eC077cB2Db80ea283683d0dF4C9A24")


