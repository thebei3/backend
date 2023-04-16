from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import json
import re

app = Flask(__name__)


@app.route('/getnewurl', methods=['GET'])
def getnewurl():
    return 'https://www.investing.com/news/cryptocurrency-news'

@app.route('/parse-news', methods=['POST'])
def parse_news():
    html_code = request.get_data(as_text=True)
    html_code = re.sub(r'\\', '', html_code)  # \ karakterlerini sil
    soup = BeautifulSoup(html_code, 'html.parser')

    titles = soup.select('.largeTitle a.title')
    dates = soup.select('.largeTitle .date')
    photo_urls = soup.select('.largeTitle img.lazyload')
    detail_urls = soup.select('.largeTitle a.img')

    news_data = []
    for title, date, photo_url, detail_url in zip(titles, dates, photo_urls, detail_urls):
        if 'ago' in date.text:
            time_ago = date.text
        else:
            time_ago = None
        
        resulltLink = ''

        if not detail_url['href'].startswith('http'):
            urlPrefix = 'https://www.investing.com'
            resulltLink = urlPrefix + detail_url['href']
            
        news_item = {
            'title': title.text,
            'timeAgo': time_ago,
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
