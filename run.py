from Eureka.api import api_run
from Eureka.db.artifact_card_db import CardDb
from Eureka.utils.GetConfig import config

if __name__ == '__main__':
    db = CardDb()
    db.init_cards_db()
    api_run()