import requests, json

version = ["00", "01"]


def get_card_set(setid):
    url = "https://playartifact.com/cardset/" + setid
    info = requests.get(url).json()
    url_deck = info["cdn_root"] + info["url"]
    return url_deck


if __name__ == '__main__':
    print(get_card_set(version[0]))
