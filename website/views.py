from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from website import cmp_api
from website import webscrap
from website import etherscan_api
from website import models
from website import mediastack
from datetime import datetime
from dateutil import parser


price_dict = cmp_api.get_price_data()

search_terms = ['bitcoin-news/', 'ethereum-news/', 'nft-news/']

links_bitcoin = webscrap.scrape(search_terms[0])

links_ethereum = webscrap.scrape(search_terms[1])

links_nft = webscrap.scrape(search_terms[2])

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    address = "0x6BF65C8278674FE0F6EF847c3eea95f3b8481178"
    transaction_list = etherscan_api.etherscan_transactions(address)
    erc20_transaction_list = etherscan_api.erc20_transactions(address)

    gas_price_dict = etherscan_api.etherscan_gas()
    gas_total = etherscan_api.find_total_gas_spent(transaction_list)
    fav_coins = etherscan_api.find_fav_coins(erc20_transaction_list)

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
                           highest_gas=highest_gas,
                           average_gas_ethereum=average_gas_ethereum,
                           average_gas_erc20=average_gas_erc20)


@views.route('/news')
def news():
    return render_template('news.html',
                           user=current_user,
                           links_bitcoin=links_bitcoin,
                           links_ethereum=links_ethereum,
                           links_nft=links_nft)



@views.route('/news2')
def news2():
    bitcoin_stream = mediastack.mediastack_scrape('bitcoin')
    ethereum_stream = mediastack.mediastack_scrape('ethereum')
    altcoin_stream = mediastack.altcoin_news()
    current_time = parser.parse(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    return render_template('news2.html',
                           user=current_user,
                           bitcoin_stream=bitcoin_stream,
                           ethereum_stream=ethereum_stream,
                           altcoin_stream=altcoin_stream,
                           current_time=current_time)


@views.route('/transactions')
def transactions():
    address = "0x6BF65C8278674FE0F6EF847c3eea95f3b8481178"
    transaction_list = etherscan_api.etherscan_transactions(address)
    erc20_transaction_list = etherscan_api.erc20_transactions(address)
    transaction_table_headings = ['Date created', 'Hash', 'To', 'From', 'Value', 'Token Involved', 'Gas Price', 'Gas Spent']
    
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
