from bs4 import BeautifulSoup
import requests


#  function can take parameters such as bitcoin-news, ethereum-news, nft-news
def scrape(term):
    source = requests.get('https://cryptonews.com/news/' + term).text

    soup = BeautifulSoup(source, 'lxml')

    results = soup.find_all('div', class_='props')

    links = []

    #  adds news links to array but the base URL still needs to be added before functional
    for result in results:
        links.append(result.h4.a)
    
    return links



