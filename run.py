from Eureka.Api.api import api_run
from Eureka.DeckManager.artifact_card_db import CardDb

if __name__ == '__main__':
    db = CardDb()
    db.init_cards_db()
    api_run()