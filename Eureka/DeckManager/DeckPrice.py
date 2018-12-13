from Eureka.SteamMarket.MarketPrice import get_market_current_lowest_price
from Eureka.DeckManager.DeckDecoder import CADD
from Eureka.DeckManager.DeckManager import DeckManager


class DeckPrice(object):
    def __init__(self, deck_code):
        self.tootle_price = 0
        self.deck_code = deck_code
        self.name = ""
        self.heroes = []
        self.cards = []
        self.status = {}
        self.deck_manager = DeckManager()

    def get_deck_price_json(self):
        """
        get_deck_price_json
        :return: 返回卡组价格信息 json 格式
        """
        try:
            deck_code_json = CADD.parse_deck(self.deck_code)
        except ValueError as e:
            self.status["ok"] = "error"
            self.status["msg"] = str(e)
            return {"status": self.status}
        self.name = deck_code_json["name"]
        self.get_heroes_price(deck_code_json["heroes"])
        self.get_cards_price(deck_code_json["cards"])
        self.status["ok"] = "ok"
        self.status["msg"] = ""
        return {
            "status": self.status,
            "name": self.name,
            "heroes": self.heroes,
            "cards": self.cards,
            "tootle_price": format(self.tootle_price, "0.01f")
        }

    def get_heroes_price(self, heroes):
        for hero in heroes:
            hero_price_info = {}
            id = hero["id"]
            hero_price_info["id"] = id
            hero_price_info["name"] = self.deck_manager.get_card_name(id)
            item_def = self.deck_manager.get_item_def(id)
            if item_def:
                hero_price_info["single_price"] = get_market_current_lowest_price(item_def)
                self.tootle_price += float(hero_price_info["single_price"].strip("¥"))
            else:
                hero_price_info["single_price"] = "Base Card"
            self.heroes.append(hero_price_info)

    def get_cards_price(self, cards):
        for card in cards:
            card_price_info = {}
            id = card["id"]
            card_price_info["id"] = id
            card_price_info["name"] = self.deck_manager.get_card_name(id)
            item_def = self.deck_manager.get_item_def(id)
            if item_def:
                card_price_info["single_price"] = get_market_current_lowest_price(item_def)
                self.tootle_price +=float(card_price_info["single_price"].strip("¥")) * float(card["count"])
            else:
                card_price_info["single_price"] = "Base Card"
            self.cards.append(card_price_info)


if __name__ == "__main__":
    deck_price = DeckPrice("ADCJYsSJLkCgxhLC7hdQmTdAU6CipuiAWkBdgENsQGGYQPpu5HnuqLmiZPpkrEgLSBEb2c_")
    print(deck_price.get_deck_price_json())
