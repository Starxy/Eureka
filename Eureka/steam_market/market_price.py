import requests
from Eureka.utils.GetConfig import config


def get_proxy():
    enable = config.socks5_enable()
    if enable != '1':
        return {}
    if config.socks5_username():
        socks5 = "{}:{}@{}".format(config.socks5_username(), config.socks5_password(), config.socks5_ip())
    else:
        socks5 = config.socks5_ip()
    proxies = {
        'http': 'socks5://' + socks5,
        'https': 'socks5://' + socks5,
    }
    return proxies


def get_market_current_lowest_price(item_def, currency="23"):
    url = "https://steamcommunity.com/market/priceoverview"
    proxies = get_proxy()

    # url = "http://ip.starxy.cc"
    postData = {
        "appid": "583950",
        "market_hash_name": item_def,
        "currency": currency
    }
    price_info = requests.get(url=url, params=postData, proxies=proxies).json()
    return price_info["lowest_price"]


if __name__ == '__main__':
    print(get_proxy())
