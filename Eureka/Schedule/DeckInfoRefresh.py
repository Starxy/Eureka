from apscheduler.schedulers.background import BackgroundScheduler
from Eureka.DeckManager.DeckManager import DeckManager
import time

def schedule_refresh():
    deck_manager = DeckManager()
    deck_manager.refresh()


def run():
    schedule_refresh()
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_refresh, 'interval', hours=1)
    scheduler.start()

    while True:
        time.sleep(3)
