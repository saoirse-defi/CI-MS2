import requests 

# API key for etherscan
API_KEY = "PQWGH496A8A1H3YV5TKWNVCPHJZ3S7ITHA"  

# sample ethereum address
address = "0x2158bC4E35eC077cB2Db80ea283683d0dF4C9A24"

# api request url outlined by etherscan
url = "https://api.etherscan.io/api?module=account&action=txlist&address="\
    + address + \
    "&startblock=0&endblock=99999999&sort=asc&apikey=" + API_KEY  

# uses requests import to issue a GET request
response = requests.get(url)

# parses into json
response_json = response.json()

# GET the 'result' section of the request
transactions = response_json.get("result")

# Print each transaction in the transactions array
for transaction in transactions:
    print(transaction)

