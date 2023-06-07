import request 
from bs4 import BeautifulSoup
import csv 


import requests

cookies = {
    '_ga': 'GA1.2.1721016650.1681630284',
    '_ym_uid': '1681630285137061412',
    '_ym_d': '1681630285',
    'PHPSESSID': 'odleh9ff3qnqeppovqp5ijar5g',
    'astratop': '1',
    '_gid': 'GA1.2.555531744.1681754406',
    '_ym_isad': '2',
    '_gat': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://stroka.kg/kupit-kvartiru/',
    'Alt-Used': 'stroka.kg',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.1721016650.1681630284; _ym_uid=1681630285137061412; _ym_d=1681630285; PHPSESSID=odleh9ff3qnqeppovqp5ijar5g; astratop=1; _gid=GA1.2.555531744.1681754406; _ym_isad=2; _gat=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://stroka.kg/kupit-kvartiru/?q&order=cost&cost_min&cost_max', cookies=cookies, headers=headers)


response = requests.get("https://stroka.kg/", cookies=cookies, headers=headers)

soup = BeautifulSoup('response.text', 'html.parser')

