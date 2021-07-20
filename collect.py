from bs4 import BeautifulSoup
import requests
import time
from models import db, Product
import re


def search(get_url, products, search_key):
    html = requests.get(get_url)
    soup = BeautifulSoup(html.text, 'lxml')
    # print(html.status_code)
    # content = soup.find_all(class_="VZTCjd")
    content = soup.find_all(class_="P8xhZc")
    # content = soup.find_all(class_="LNwFVe")
    for i in content:
        # print(i)
        # print(i.find('a').text)
        print(i.find('a').get('href'))
        # print(i.find('span',class_='HRLxBb').text)
        # products.append(Product(name=i.find('a').text,price=i.find('span',class_='HRLxBb').text,seller_url=i.find('a').get('href'),companies='sample',evaluation_value))
        price = re.sub(r"\D", "", i.find('span', class_='HRLxBb').text)
        seller_url = i.find('a').get('href').replace('/url?q=', '')
        print('#'*10)
        print(seller_url)
        print('#'*10)
        db.session.add(Product(
            i.find('a').text,
            price,
            seller_url,
            'companie',
            4.4,
            search_key
        )
        )
        print(i.find('a').text)
    time.sleep(1.5)
    print('############################\n',
          get_url, '\n############################')
    # print(soup)
    if content:
        return html.status_code
    else:
        return 400


def collect_product(search_key):
    search_key = search_key
    num = 0
    status = 200
    url = 'https://www.google.com/search?q={}&tbm=shop&start={}'.format(
        search_key, num)
    products = []
    for _ in range(1):
        if status == 200:
            status = search(url, products, search_key)
        else:
            break
        num += 20
        url = 'https://www.google.com/search?q={}&tbm=shop&start={}'.format(
            search_key, num)
    db.session.commit()


# collect_product('cola')
