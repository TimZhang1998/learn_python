from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ErrorInResponseException
# import demjson
import requests
import json
import re

def get_page_index(offset, keyword):
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
    browser = webdriver.Chrome()
    try:
        browser.get(url)
        return browser.page_source
    except ErrorInResponseException:
        print('url response error')
    finally:
        browser.close()    
    '''
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'}
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('request detail error', url)
        return None
    '''

def page_detail_parse(html, url):
    data = []
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    '''
    images_pattern = re.compile(r'gallery: JSON.parse\("(.*?|\n)"\)', re.S)
    result = re.search(images_pattern, html)
    if result:
        data = json.loads(result.group(1))
        # data = demjson.decode(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            return {
                'title': title,
                'url': url,
                'image': images
                }
    '''
    images_pattern = re.compile('<img src="(.*?)" data-src="(.*?)" alt="" />', re.S)
    results = re.findall(images_pattern, html)
    if results:
        for result in results:
            image = result[1]
            data.append(image)
        if data:
            return {
                'title': title,
                'url': url,
                'image': data
                }

def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        if url:
            html = get_page_detail(url)
            print(html)
            if html:
                result = page_detail_parse(html, url)
                print(result)

if __name__ == '__main__':
    main()
    