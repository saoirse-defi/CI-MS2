from flask import request
import requests
import time
from datetime import datetime, timezone, date
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
                'published': parser.parse(data['published_at']).strftime("%Y-%m-%d %H:%M:%S")
            }

            article_list.append(article)

    return article_list


def altcoin_news(token_list):
    altcoin_article_list = []

    for token in token_list:
        if(mediastack_scrape(token) is not None):
            for item in mediastack_scrape(token):
                if token not in item['title']:
                    continue
                else:
                    altcoin_article_list.append(item)
    return altcoin_article_list
