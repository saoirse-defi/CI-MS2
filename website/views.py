from flask import Blueprint, render_template
from flask_login import current_user, login_required
from website import cmp_api
from website import webscrap


price_dict = cmp_api.get_price_data()

search_terms = ['bitcoin-news/', 'ethereum-news/', 'nft-news/']

links_bitcoin = webscrap.scrape(search_terms[0])

links_ethereum = webscrap.scrape(search_terms[1])

links_nft = webscrap.scrape(search_terms[2])

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template('home.html',
                           user=current_user,
                           price_dict=price_dict)


@views.route('/news')
def news():
    return render_template('news.html',
                           user=current_user,
                           links_bitcoin=links_bitcoin,
                           links_ethereum=links_ethereum,
                           links_nft=links_nft)



