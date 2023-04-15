from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import json


app = Flask(__name__)


@app.route('/parse-news', methods=['POST'])
def parse_news():
    html_code = request.get_data(as_text=True)
    soup = BeautifulSoup(html_code, 'html.parser')

    titles = soup.find_all('a', class_='title')
    photo_urls = soup.find_all('img', class_='lazyload')
    detail_urls = soup.find_all('a', class_='img')

    news_data = []
    for title, photo_url, detail_url in zip(titles, photo_urls, detail_urls):
        news_item = {
            'title': title.text,
            'photoUrl': photo_url['data-src'],
            'linkUrl': detail_url['href']
        }
        news_data.append(news_item)

    # `news_data` verisini JSON formatına dönüştürüyoruz
    json_data = json.dumps(news_data)

    # JSON verisini geri döndürüyoruz
    return jsonify(json_data)
