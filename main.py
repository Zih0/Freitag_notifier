import json
import requests
import time
from telegram_bot import TelegramBot
from bs4 import BeautifulSoup

# from stem import Signal
# from stem.control import Controller

found = []

session = requests.session()
soup = BeautifulSoup(
    session.get("https://www.freitag.ch/authcache.php?a=&r=frag/panels/neo-menu-user-bar&o%5Bq%5D=en/&v=null").content,
    features='html5lib')
loginForm = soup.find('form', attrs={'id': 'user-login'})
auth = loginForm.find_all('input', attrs={'type': 'hidden'})[0]

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

Furl = 'https://www.freitag.ch/en'

header = {
    # header..
    'Referer': 'https://www.freitag.ch/en',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

data = {
    # data.. Login
    'name': 'id',
    'pass': 'password',
    'form_build_id': auth['value'],
    'form_id': 'user_login',
    'op': 'Log in'
}


def check():
    url = "https://www.freitag.ch/en/json/model/1732/products/0/0"
    response = requests.get(url, proxies=proxies)
    response.encoding = "utf-8"
    result = response.json()
    for product in result["products"]:
        product_id = product["product"]["product_id"]
        if product_id not in found:
            found.append(product_id)


def HawaiiFive():
    url = "https://www.freitag.ch/en/json/model/1732/products/0/0"
    response = requests.get(url, proxies=proxies)
    response.encoding = "utf-8"
    result = response.json()
    for product in result["products"]:
        imgUrl = product["product"]["neo_product_cover_photo"]["src"]
        product_id = product["product"]["product_id"]
        if product_id not in found:
            bot.sendMessage(receiver_id, imgUrl)
            bot.sendMessage(receiver_id, "https://www.freitag.ch/en/f41?productID=" + product_id)
            if product['product']['neo_product_colors'] == 'black':
                session.post(Furl, headers=header, data=data)
                session.get('https://www.freitag.ch/en/cart/add/' + product_id + '/1')
                bot.sendMessage(myid, "https://www.freitag.ch/en/checkout/")
            if product['product']['neo_product_colors'] == 'patina white' and product['product'][
                'neo_product_style'] == 'plain':
                session.post(Furl, headers=header, data=data)
                session.get('https://www.freitag.ch/en/cart/add/' + product_id + '/1')
                bot.sendMessage(myid, "https://www.freitag.ch/en/checkout/")
            if product['product']['neo_product_colors'] == 'snow white' and product['product'][
                'neo_product_style'] == 'plain':
                session.post(Furl, headers=header, data=data)
                session.get('https://www.freitag.ch/en/cart/add/' + product_id + '/1')
                bot.sendMessage(myid, "https://www.freitag.ch/en/checkout/")
            found.append(product_id)


# def renew_tor_ip():
#     with Controller.from_port(port=9051) as controller:
#         controller.authenticate(password="password")
#         controller.signal(Signal.NEWNYM)


if __name__ == "__main__":

    token = 'token'  # your token
    myid = 'id' # personal id
    receiver_id = 'id'  # group id
    bot = TelegramBot(token)
    check()
    num = 0
    while num < 3200:
        HawaiiFive()
        time.sleep(1.5)
        num += 1
        # if num % 2 == 0:
        #     renew_tor_ip()
