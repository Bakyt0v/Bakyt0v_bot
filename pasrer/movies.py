import requests
from bs4 import  BeautifulSoup
from random import randint,random
from requests_html import HTMLSession

URL = 'https://w139.zona.plus/'

HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
# H           o            m          e           w           r          k   ----------N__E__X__T---------------------->
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_="results-item-wrap")
    movie = []



    for item in items:
        movie.append(
            {"title":URL + item.find('a', class_='results-item').get('href'),
             "image":item.find("meta", itemprop="image").get('content'),
             # 'name':item.find('div', class_='results-item-title').get('results-item-title')
            }
        )
    return movie[0].values()


def parser():
    html  = get_html(URL)
    if html.status_code == 200:
        movie = []
        for page in range(0, 5):
            html = get_html(f"https://w139.zona.plus/movies/filter/year-2022/latset/{page}")
            movie.extend(get_data(html.text))
        return movie
    else:
        raise Exception('Error in parser function')
# parser()
# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
# ============================H++++++++++E+++++++++++R+++++++++++E======================================================
