import requests
import redis


class CardDb:
    def __init__(self,host,port,name):
        self.r = redis.Redis(host=host, port=port, db=name)
        self.version = ["00", "01"]

    def get_card_set_info(self, setid):
        url = "https://playartifact.com/cardset/" + setid
        info = requests.get(url).json()
        url_deck = info["cdn_root"] + info["url"]
        return requests.get(url_deck).json()

    def set_card_hashs(self, card):
        if 'rarity' in card and 'item_def' in card:
            self.r.hmset(card['card_id'], {'card_id': card['card_id'], 'card_name': card['card_name']['schinese'],
                                           'rarity': card['rarity'], 'item_def': card['item_def']})
        else:
            self.r.hmset(card['card_id'], {'card_id': card['card_id'], 'card_name': card['card_name']['schinese']})

    def init_cards_db(self, ):
        for setid in self.version:
            for card in self.get_card_set_info(setid)['card_set']['card_list']:
                self.set_card_hashs(card)

    def get_item_def_by_card_id(self, card_id):
        return self.r.hget(self, card_id, 'item_def')

    def get_card_name_by_card_id(self, card_id):
        return self.r.hget(card_id, 'card_name')


if __name__ == '__main__':
    pass
