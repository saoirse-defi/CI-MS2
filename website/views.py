from flask import Blueprint, render_template
from flask_login import current_user, login_required
from website import coinmarketcap_api
from website import cmp_api

#  pull in api data and display as a 2 decimal float
bitcoin_price = "{:.2f}".format(coinmarketcap_api.get_coin_price('BTC'))
ethereum_price = "{:.2f}".format(coinmarketcap_api.get_coin_price('ETH'))
litecoin_price = "{:.2f}".format(coinmarketcap_api.get_coin_price('LTC'))

price_dict = cmp_api.get_price_data()

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template('home.html',
                           user=current_user, 
                           bitcoin_price=bitcoin_price, 
                           ethereum_price=ethereum_price,
                           litecoin_price=litecoin_price,
                           price_dict=price_dict)



