import requests


def get_market_current_lowest_price(item_def, currency="23"):
    url = "https://steamcommunity.com/market/priceoverview"
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080',
    }
    # url = "http://ip.starxy.cc"
    postData = {
        "appid": "583950",
        "market_hash_name": item_def,
        "currency": currency
    }
    price_info = requests.get(url=url, params=postData, proxies=proxies).json()
    return price_info["lowest_price"]


if __name__ == '__main__':
    print(get_market_current_lowest_price(110425))
