from flask import request
import requests
import time
from datetime import datetime, timezone
from dateutil import parser
from promise import Promise


def mediastack_scrape(keyword):
    API_KEY = "191f63f844300b21e5471668e31c36b2"
    todays_date = time.strftime('%Y-%m-%d')  # get today's date for api request

    url = "http://api.mediastack.com/v1/news?access_key=" + API_KEY + "&date=" + todays_date + "&languages=en&limit=10&sort=popularity&keywords=" + keyword

    response = requests.get(url)
    response_json = response.json()
    data_stream = response_json.get("data")

    article_list = []

    if (data_stream is not None):
        for data in data_stream:
            article = {
                'author': data['author'],
                'title': data['title'],
                'description': data['description'],
                'url': data['url'],
                'source': data['source'],
                'published': parser.parse(data['published_at'])
            }

            article_list.append(article)

    return article_list


def altcoin_news(token_list):
    #  token_names = ['cardano', 'polkadot', 'binance', 'litecoin', 'dogecoin', 'XRP', 'uniswap', 'solana', 'chainlink']
    altcoin_article_list = []

    for token in token_list:
        if(mediastack_scrape(token) is not None):
            for item in mediastack_scrape(token):
                if token not in item['title']:
                    altcoin_article_list.append(item)
                else:
                    continue

    return altcoin_article_list
