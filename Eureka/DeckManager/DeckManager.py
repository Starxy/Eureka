from Eureka.DeckManager.GetDeckJsonData import get_deck_json
from Eureka.DB.DbClient import DbClient


class DeckManager(object):
    """
    DeckManager
    """

    def __init__(self):
        self.db = DbClient()
        self.version = ["00", "01"]

    def refresh(self):
        for set_id in self.version:
            for card in get_deck_json(set_id)['card_set']['card_list']:
                self.db.hset(card["card_id"], 'card_id', card["card_id"])
                self.db.hset(card["card_id"], 'card_name', card["card_name"]["schinese"])
                self.db.hset(card["card_id"], 'rarity', card["rarity"] if "rarity" in card else "")
                self.db.hset(card["card_id"], 'item_def', card["item_def"] if "item_def" in card else "")

    def get_card_name(self, card_id):
        return self.db.get_card_name(card_id)

    def get_item_def(self, card_id):
        return self.db.get_item_def(card_id)


if __name__ == '__main__':
    DeckManager = DeckManager()
    # DeckManager.refresh()
    print(DeckManager.get_card_name(10002))
    print(DeckManager.get_item_def(10002))
