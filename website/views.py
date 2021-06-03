from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from website import cmp_api
from website import webscrap
from website import etherscan_api
from website import models


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
    transaction_table_headings = ['Date created', 'To', 'From', 'Value', 'Gas Price', 'Gas Spent']

    def shorten(string):
        return "0x..." + string[38:]

    def toInt(x):
        return int(float(x))

    def threeDecimals(y):
        return "%.3f" % y

    return render_template('home.html',
                           user=current_user,
                           price_dict=price_dict,
                           transaction_list=transaction_list,
                           transaction_table_headings=transaction_table_headings,
                           address=address,
                           shorten=shorten,
                           toInt=toInt,
                           threeDecimals=threeDecimals)


@views.route('/news')
def news():
    return render_template('news.html',
                           user=current_user,
                           links_bitcoin=links_bitcoin,
                           links_ethereum=links_ethereum,
                           links_nft=links_nft)



