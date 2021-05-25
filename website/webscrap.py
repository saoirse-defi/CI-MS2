from bs4 import BeautifulSoup
import requests


#  function can take parameters such as bitcoin-news, ethereum-news, nft-news
def scrape(term):
    source = requests.get('https://cryptonews.com/news/' + term).text

    soup = BeautifulSoup(source, 'lxml')

    results = soup.find_all('div', class_='article')

    news_list = []

    #  adds news links to array but the base URL 
    #  still needs to be added before functional
    for result in results:

        news = {
            'link': 'https://cryptonews.com/news' + result.a['href'],
            'text': result.h4.text,
        }

        news_list.append(news)

    return news_list
