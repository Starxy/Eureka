from flask import Flask,json,jsonify
from decode import decode
import artifact_card_db
import market_price

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome To Artifact Market Plugin"


@app.route("/code/<deck_code>")
def code_to_deck(deck_code):
    deck_json = decode(deck_code)
    heros_price = []
    cards_price = []
    deck_price = {}
    sum_price = 0
    for hero in deck_json["heroes"]:
        new_hero_info = {}
        id = hero["id"]
        new_hero_info["id"] = id
        new_hero_info["name"] = artifact_card_db.get_card_name_by_card_id(id).decode("utf-8")
        item_def = artifact_card_db.get_item_def_by_card_id(id)
        if item_def:
            new_hero_info["single_price"] = market_price.get_market_current_lowest_price(item_def)
            sum_price = sum_price + float(new_hero_info["single_price"].strip("¥"))
        else:
            new_hero_info["single_price"] = "Base Card"
        heros_price.append(new_hero_info)

    for card in deck_json["cards"]:
        new_card_info = {}
        id = card["id"]
        new_card_info["id"] = id
        new_card_info["name"] = artifact_card_db.get_card_name_by_card_id(id).decode("utf-8")
        item_def = artifact_card_db.get_item_def_by_card_id(id)
        if item_def:
            new_card_info["single_price"] = market_price.get_market_current_lowest_price(item_def)
            sum_price = sum_price + float(new_card_info["single_price"].strip("¥")) * float(card["count"])
        else:
            new_card_info["single_price"] = "Base Card"
        cards_price.append(new_card_info)
    deck_price["heros"] = heros_price
    deck_price["cards"] = cards_price
    deck_price["sum"] = sum_price
    return jsonify(deck_price)

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
