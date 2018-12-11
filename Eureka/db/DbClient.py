from Eureka.Utils.GetConfig import config
from Eureka.Utils.utilClass import Singleton
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class DbClient(object):
    """
    DB 工厂类
    提供方法：
        hash存储

    """
    __metaclass__ = Singleton

    def __init__(self):
        self.__initDbClient()

    def __initDbClient(self):

        __type = None
        if "redis" == config.db_type.lower():
            __type = "RedisClient"
        else:
            pass
        assert __type, 'type error, Not support DB type: {}'.format(config.db_type)
        self.client = getattr(__import__(__type), __type)(name=config.db_name, host=config.db_host, port=config.db_port)

    def hset(self, name, key, value):
        return self.client.hset(name, key, value)

    def get_item_def(self, name):
        return self.client.get_item_def(name)

    def get_card_name(self, name):
        return self.client.get_card_name(name)
