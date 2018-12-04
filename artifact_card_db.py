import requests, redis
import config

r = redis.Redis(host=config.db_host, port=config.db_port, db=config.db_name)

version = ["00", "01"]


def get_card_set_info(setid):
    url = "https://playartifact.com/cardset/" + setid
    info = requests.get(url).json()
    url_deck = info["cdn_root"] + info["url"]
    return requests.get(url_deck).json()


def set_card_hashs(card):
    if 'rarity' in card and 'item_def' in card:
        r.hmset(card['card_id'], {'card_id': card['card_id'], 'card_name': card['card_name']['schinese'],
                                  'rarity': card['rarity'], 'item_def': card['item_def']})
    else:
        r.hmset(card['card_id'], {'card_id': card['card_id'], 'card_name': card['card_name']['schinese']})


def init_cards_db():
    for setid in version:
        for card in get_card_set_info(setid)['card_set']['card_list']:
            set_card_hashs(card)


def get_item_def_by_card_id(card_id):
    return r.hget(card_id, 'item_def')


def get_card_name_by_card_id(card_id):
    return r.hget(card_id, 'card_name')


if __name__ == '__main__':
    init_cards_db()
