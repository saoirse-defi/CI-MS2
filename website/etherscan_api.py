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
            'time': time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(int(transaction['timeStamp']))),
            'from': transaction['from'],
            'to': transaction['to'],
            'value': Web3.fromWei(int(transaction['value']), 'ether'),  # in Gwei
            'error': transaction['isError'],
            'gas_price': Web3.fromWei(int(transaction['gasPrice']), 'ether') * int('1000000000'),
            'gas_used': Web3.fromWei(int(transaction['gasPrice']) * int(transaction['gasUsed']), 'ether')
        }
        transaction_list.append(data)
    
    return transaction_list
