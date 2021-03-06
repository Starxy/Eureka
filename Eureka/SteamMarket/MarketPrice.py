import requests
from Eureka.Utils.SteamProxy import proxy
from Eureka.Utils.LogHandle import LogHandler

log = LogHandler("MarketPrice")


def get_market_current_lowest_price(item_def, appid="583950", currency="23"):
    """
    从 Steam 商店获取价格信息
    :param appid: 游戏 id 默认为 Artifact
    :param item_def: 物品 id
    :param currency: 返回价格结算货币 默认 23 为 RMB
    :return: 当前最低价格
    """
    url = "https://steamcommunity.com/market/priceoverview"
    proxies = proxy.get_proxy()
    post_data = {
        "appid": appid,
        "market_hash_name": item_def,
        "currency": currency
    }
    try:
        price_info = requests.get(url=url, params=post_data, proxies=proxies).json()
        return price_info["lowest_price"]
    except Exception as e:
        log.error(e)
        raise RuntimeError("Steam 商店请求暂时不可用")


if __name__ == '__main__':
    print(get_market_current_lowest_price(110001))
