from api import app
import artifact_card_db

if __name__ == '__main__':
    artifact_card_db.init_cards_db()
    app.run()
