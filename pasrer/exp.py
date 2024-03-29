import requests
from bs4 import  BeautifulSoup


URL = 'https://etnomedia.kg/movies/category/115'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
# H           o            m          e           w           r          k   ----------N__E__X__T---------------------->
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="container")
    movie = []
    print(items)

    for item in items:
        movie.append(
            {
             "title":URL + item.find('a', class_='VideoCard_title__2SCab').find("a").get('href')
             # "image":URL + item.find('li', class_="lazyload-wrapper").find("img").get("src")
            }
        )
    return movie


def parser():
    html  = get_html(URL)
    if html.status_code == 200:
        movie = []
        for page in range(0, 1):
            html = get_html(f"https://etnomedia.kg/movies/category/115/latset/{page}")
            movie.extend(get_data(html.text))
        return movie
    else:
        raise Exception('Error in parser function')
parser()
# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
# ============================H++++++++++E+++++++++++R+++++++++++E======================================================
