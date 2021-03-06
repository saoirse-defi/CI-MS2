from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from website import cmp_api
from website import webscrap
from website import etherscan_api
from website import models
from website import mediastack
from datetime import datetime, date
import time
from dateutil import parser

address = "0x6BF65C8278674FE0F6EF847c3eea95f3b8481178"
transaction_list = etherscan_api.etherscan_transactions(address)
erc20_transaction_list = etherscan_api.erc20_transactions(address)
fav_coin_names = etherscan_api.find_fav_coin_names(erc20_transaction_list)

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    gas_price_dict = etherscan_api.etherscan_gas()
    gas_total = etherscan_api.find_total_gas_spent(transaction_list)
    fav_coins = etherscan_api.find_fav_coins(erc20_transaction_list)
    fav_token = etherscan_api.find_fav_token(erc20_transaction_list)
    price_dict = cmp_api.get_price_data(fav_coins)
    highest_gas_eth = etherscan_api.find_highest_gas(transaction_list)
    highest_gas_erc20 = etherscan_api.find_highest_gas(erc20_transaction_list)
    highest_gas = int(max(highest_gas_eth, highest_gas_erc20))
    average_gas_ethereum = etherscan_api.find_average_gas(transaction_list)
    average_gas_erc20 = etherscan_api.find_average_gas(erc20_transaction_list)

    def toInt(x):
        return int(float(x))

    def threeDecimals(y):
        return "%.3f" % y

    return render_template('home.html',
                           user=current_user,
                           price_dict=price_dict,
                           gas_price_dict=gas_price_dict,
                           gas_total=gas_total,
                           erc20_transaction_list=erc20_transaction_list,
                           fav_coins=fav_coins,
                           fav_token=fav_token,
                           fav_coin_names=fav_coin_names,
                           highest_gas=highest_gas,
                           average_gas_ethereum=average_gas_ethereum,
                           average_gas_erc20=average_gas_erc20)


@views.route('/news2')
def news2():
    bitcoin_stream = mediastack.mediastack_scrape('bitcoin')
    ethereum_stream = mediastack.mediastack_scrape('ethereum')
    altcoin_stream = mediastack.altcoin_news(fav_coin_names)

    current_time = datetime.now() # still need to subtract time to show time elapsed

    return render_template('news2.html',
                           user=current_user,
                           bitcoin_stream=bitcoin_stream,
                           ethereum_stream=ethereum_stream,
                           altcoin_stream=altcoin_stream,
                           current_time=current_time)


@views.route('/nft')
def nft():
    address = "0x72BFb4d1Ae160552B44F9c99Ff56d9311b5941f4"
    nft_stream = etherscan_api.nft_transactions(address)
    transaction_table_headings = ['Date created', 'Hash', 'To', 'From', 'Token ID', 'Token Involved', 'Gas Price (GWEI)', 'Gas Spent (ETH)']
    
    def shorten2(string):
        return "0x..." + string[62:]

    def shorten(string):
        return "0x..." + string[38:]

    def toInt(x):
        return int(float(x))

    def threeDecimals(y):
        return "%.3f" % y

    return render_template('nft.html',
                           user=current_user,
                           nft_stream=nft_stream,
                           transaction_table_headings=transaction_table_headings,
                           shorten=shorten,
                           shorten2=shorten2,
                           toInt=toInt,
                           threeDecimals=threeDecimals)


@views.route('/transactions')
def transactions():
    address = "0x6BF65C8278674FE0F6EF847c3eea95f3b8481178"
    transaction_list = etherscan_api.etherscan_transactions(address)
    erc20_transaction_list = etherscan_api.erc20_transactions(address)
    transaction_table_headings = ['Date created', 'Hash', 'To', 'From', 'Value', 'Token Involved', 'Gas Price (GWEI)', 'Gas Spent (ETH)']    

    def shorten(string):
        return "0x..." + string[38:]
    
    def shorten2(string):
        return "0x..." + string[62:]

    def toInt(x):
        return int(float(x))

    def threeDecimals(y):
        return "%.3f" % y

    return render_template('transactions.html',
                           user=current_user,
                           transaction_list=transaction_list,
                           erc20_transaction_list=erc20_transaction_list,
                           transaction_table_headings=transaction_table_headings,
                           address=address,
                           shorten=shorten,
                           shorten2=shorten2,
                           toInt=toInt,
                           threeDecimals=threeDecimals
                           )
