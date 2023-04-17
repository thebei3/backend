from flask import Flask, request, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import json
import re
import html5lib

app = Flask(__name__)


@app.route('/getnewurl_usa', methods=['GET'])
def getnewurl_usa():
    return 'https://www.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_tr', methods=['GET'])
def getnewurl_tr():
    return 'https://tr.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_it', methods=['GET'])
def getnewurl_it():
    return 'https://it.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_es', methods=['GET'])
def getnewurl_es():
    return 'https://es.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_cn', methods=['GET'])
def getnewurl_cn():
    return 'https://cn.investing.com/news/cryptocurrency-news'


@app.route('/getnewurl_fr', methods=['GET'])
def getnewurl_fr():
    return 'https://fr.investing.com/news/cryptocurrency-news'


@app.route('/parse-news', methods=['POST'])
def parse_news():
    data = json.loads(request.get_data(as_text=True))
    baseUrl = re.sub(r'/news/cryptocurrency-news', '', data['baseUrl'])
    html_code = data['html_code']
    html_code = re.sub(r'\\', '', html_code)  # \ karakterlerini sil
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

    # `news_data` verisini JSON formatına dönüştürüyoruz
    json_data = json.dumps(news_data)

    # JSON verisini geri döndürüyoruz
    return json_data


if __name__ == '__main__':
    app.run()
