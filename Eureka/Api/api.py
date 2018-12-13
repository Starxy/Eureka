from flask import Flask, jsonify
from Eureka.DeckManager.DeckPrice import DeckPrice
from Eureka.Utils.GetConfig import config

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome To Artifact Market Plugin"


@app.route("/code/<deck_code>")
def code_to_deck(deck_code):
    deck_price = DeckPrice(deck_code).get_deck_price_json()
    if deck_price["status"]["ok"] == "ok":
        return jsonify(deck_price)
    else:
        return jsonify(deck_price["status"])


def api_run():
    app.config['JSON_AS_ASCII'] = False
    app.run(host=config.api_host, port=config.api_port)
