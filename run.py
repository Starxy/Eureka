from multiprocessing import Process
from Eureka.Api.api import api_run as api_run
from Eureka.Schedule.DeckInfoRefresh import run as refresh_run


def run():
    p_list = list()
    p1 = Process(target=api_run, name='ApiRun')
    p_list.append(p1)
    p2 = Process(target=refresh_run, name='RefreshRun')
    p_list.append(p2)

    for p in p_list:
        p.daemon = True
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()
