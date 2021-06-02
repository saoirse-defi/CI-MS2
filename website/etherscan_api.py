from flask import request
import requests
import time
from web3 import Web3


def etherscan_transactions(address):
    API_KEY = "PQWGH496A8A1H3YV5TKWNVCPHJZ3S7ITHA"

    url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=0&endblock=99999999&sort=asc&apikey=" + API_KEY
          
    response = requests.get(url)
    response_json = response.json()
    transactions = response_json.get("result")

    transaction_list = []

    for transaction in transactions:
        data = {
            'time': time.time(transaction['timestamp']),
            'from': transaction['from'],
            'to': transaction['to'],
            'value': Web3.fromWei(transaction['value'], 'ether'),  # in Gwei
            'error': transaction['isError'],
            'gas_price': Web3.fromWei(transaction['gasPrice']),
            'gas_used': Web3.fromWei(transaction['gasPrice']) * Web3.fromWei(transaction['gasUsed'])
        }
        transaction_list.append(data)
    
    return transaction_list
