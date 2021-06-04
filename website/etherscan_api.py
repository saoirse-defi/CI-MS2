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
            'time': time.strftime("%d %b %Y %H:%M", time.localtime(int(transaction['timeStamp']))),
            'hash': transaction['hash'],
            'from': transaction['from'],
            'to': transaction['to'],
            'value': Web3.fromWei(float(transaction['value']), 'ether'),  # in Gwei
            'error': transaction['isError'],
            'gas_price': Web3.fromWei(int(transaction['gasPrice']), 'ether') * int('1000000000'),
            'gas_used': Web3.fromWei(int(transaction['gasPrice']) * int(transaction['gasUsed']), 'ether')
        }
        transaction_list.append(data)
    
    return transaction_list


def erc20_transactions(address):
    API_KEY = "PQWGH496A8A1H3YV5TKWNVCPHJZ3S7ITHA"
    url = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + address + "&startblock=0&endblock=999999999&sort=asc&apikey=" + API_KEY

    response = requests.get(url)
    response_json = response.json()
    erc20 = response_json.get("result")

    erc20_transaction_list = []

    for transaction in erc20:
        data = {
            'time': time.strftime("%d %b %Y %H:%M", time.localtime(int(transaction['timeStamp']))),
            'hash': transaction['hash'],
            'from': transaction['from'],
            'to': transaction['to'],
            'value': Web3.fromWei(float(transaction['value']), 'ether'),  # in Gwei
            'gas_price': Web3.fromWei(int(transaction['gasPrice']), 'ether') * int('1000000000'),
            'gas_used': Web3.fromWei(int(transaction['gasPrice']) * int(transaction['gasUsed']), 'ether'),
            'token_name': transaction['tokenName'],
            'token_symbol': transaction['tokenSymbol']
        }

        erc20_transaction_list.append(data)
    
    return erc20_transaction_list


def etherscan_gas():
    API_KEY = "PQWGH496A8A1H3YV5TKWNVCPHJZ3S7ITHA"
    url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=" + API_KEY

    response = requests.get(url)
    response_json = response.json()
    gas_price_dict = response_json.get("result")

    return gas_price_dict


def find_total_gas_spent(list):
    total = 0
    for item in list:
        total += item['gas_used']
    
    return total


