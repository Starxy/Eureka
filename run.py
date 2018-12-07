from Eureka.api import run
from Eureka.db import artifact_card_db

if __name__ == '__main__':
    artifact_card_db.init_cards_db()
    run()
