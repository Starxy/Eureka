from redis import Redis


class RedisClient(object):
    """
    Redis clinet
    """

    def __init__(self, name, host, port, **kwargs):
        """
        init connect
        :param name:
        :param host:
        :param port:
        :param kwargs:
        """
        self.t_name = name
        self.__conn = Redis(host=host, port=port, db=0, **kwargs)

    def hset(self, card_id, key, value):
        self.__conn.hset(self.t_name + ':' + str(card_id), key, value)

    def get_item_def(self, card_id):
        """
        根据 card_id 返回 item_def
        :param card_id:
        :return:
        """
        return self.__conn.hget(self.t_name + ':' + str(card_id), "item_def").decode("utf-8")

    def get_card_name(self, card_id):
        """
        根据 card_id 返回 card_name
        :param card_id:
        :return:
        """
        return self.__conn.hget(self.t_name + ":" + str(card_id), "card_name").decode("utf-8")
