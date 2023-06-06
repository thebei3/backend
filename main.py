from flask import Flask, request, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import json
import re
import html5lib

app = Flask(__name__)


@app.route('/getnewurl_usa', methods=['GET'])
def getnewurl_usa():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://www.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://www.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://www.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://www.investing.com/news/commodities-news'
    else:
        return 'https://www.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_tr', methods=['GET'])
def getnewurl_tr():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://tr.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://tr.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://tr.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://tr.investing.com/news/commodities-news'
    else:
        return 'https://tr.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_it', methods=['GET'])
def getnewurl_it():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://it.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://it.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://it.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://it.investing.com/news/commodities-news'
    else:
        return 'https://it.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_es', methods=['GET'])
def getnewurl_es():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://es.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://es.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://es.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://es.investing.com/news/commodities-news'
    else:
        return 'https://es.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_cn', methods=['GET'])
def getnewurl_cn():
    newType = request.args.get('newType')
    if newType == 'stockMarket':
        return 'https://cn.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://cn.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://cn.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://cn.investing.com/news/commodities-news'
    else:
        return 'https://cn.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_fr', methods=['GET'])
def getnewurl_fr():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://fr.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://fr.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://fr.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://fr.investing.com/news/commodities-news'
    else:
        return 'https://fr.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_ru', methods=['GET'])
def getnewurl_ru():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://ru.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://ru.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://ru.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://ru.investing.com/news/commodities-news'
    else:
        return 'https://ru.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_vi', methods=['GET'])
def getnewurl_vi():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://vn.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://vn.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://vn.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://vn.investing.com/news/commodities-news'
    else:
        return 'https://vn.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_de', methods=['GET'])
def getnewurl_de():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://de.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://de.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://de.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://de.investing.com/news/commodities-news'
    else:
        return 'https://de.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_hi', methods=['GET'])
def getnewurl_hi():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://hi.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://hi.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://hi.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://hi.investing.com/news/commodities-news'
    else:
        return 'https://hi.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_pl', methods=['GET'])
def getnewurl_pl():
    newType = request.args.get('newType')

    if newType == 'stockMarket':
        return 'https://pl.investing.com/news/stock-market-news'
    elif newType == 'economy':
        return 'https://pl.investing.com/news/economy'
    elif newType == 'ecoInd':
        return 'https://pl.investing.com/news/economic-indicators'
    elif newType == 'commodities':
        return 'https://pl.investing.com/news/commodities-news'
    else:
        return 'https://pl.investing.com/news/cryptocurrency-news'


@app.route('/parse-news', methods=['POST'])
def parse_news():
    data = json.loads(request.get_data(as_text=True))

    baseUrl = data['baseUrl'].replace('/news/cryptocurrency-news', '').replace('/news/stock-market-news', '').replace('/news/commodities-news', '').replace('/news/economic-indicators', '').replace('/news/economy', '')

    html_code = data['html_code']
    html_code = re.sub(r'\\', '', html_code)  # \ karakterlerini sil
    html_code = re.sub(r'js-external-link title', 'title', html_code)
    html_code = re.sub(r'js-external-link img', 'img', html_code)

    soup = BeautifulSoup(html_code, 'html5lib')

    titles = soup.select('.largeTitle a.title')
    dates = soup.select('.largeTitle .date')
    photo_urls = soup.select('.largeTitle img.lazyload')
    detail_urls = soup.select('.largeTitle a.img')

    news_data = []
    for title, date, photo_url, detail_url in zip(titles, dates, photo_urls, detail_urls):

        resulltLink = detail_url['href']

        if not detail_url['href'].startswith('http'):
            urlPrefix = baseUrl
            resulltLink = urlPrefix + detail_url['href']

        news_item = {
            'title': title.text,
            'timeAgo': date.text,
            'photoUrl': photo_url['data-src'],
            'linkUrl': resulltLink
        }

        news_data.append(news_item)

    filtered_items = []
    for item in news_data:
        if 'linkUrl' in item:
            if 'pro' not in item['linkUrl'] or 'offers' not in item['linkUrl']:
                filtered_items.append(item)
        else:
            filtered_items.append(item)

    # `news_data` verisini JSON formatına dönüştürüyoruz
    json_data = json.dumps(filtered_items)

    # JSON verisini geri döndürüyoruz
    return json_data


if __name__ == '__main__':
    app.run()
