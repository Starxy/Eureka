import sys

sys.path.append('.')

from multiprocessing import Process
from Eureka.Api.api import api_run as ApiRun
from Eureka.Schedule.DeckInfoRefresh import run as RefreshRun


def run():
    p_list = list()
    p1 = Process(target=ApiRun, name='ApiRun')
    p_list.append(p1)
    p2 = Process(target=RefreshRun, name='RefreshRun')
    p_list.append(p2)

    for p in p_list:
        p.daemon = True
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()