from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import requests
import json
import re


def get_page_index(offset, keywods):
    data = {
        'offset': 0,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('request index error', url)
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('request detail error', url)
        return None

def page_detail_parse(html):
    soup = BeautifulSoup(html, 'lxml')
    # title = soup.select('title')[1].get_text()
    # print(title)
    images_pattern = re.compile('var gallery = (.*?);', re.S)
    result = re.search(images_pattern, html)
    if result:
        print(result.group(1))

def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            print(html)

if __name__ == '__main__':
    main()
    