from Eureka.api import api_run
from Eureka.db.artifact_card_db import CardDb
from Eureka.utils.GetConfig import config

if __name__ == '__main__':
    api_run()
    db = CardDb(host=config.db_host(), port=config.db_port(), name=config.db_name())
