from Eureka.Utils.GetConfig import config


class Proxy(object):
    """
    为 SteamAPI 添加代理增加的类
    目前仅添加 socks5 支持
    """

    def __init__(self):
        self.__proxy_type = None
        self.enable = True if config.proxy_enable.lower() == "true" else False
        if 'socks5' == config.proxy_type:
            self.__proxy_type = 'socks5_proxy'
        else:
            pass
        if self.enable:
            assert self.__proxy_type, 'type error, Not support Proxy type: {}'.format(config.proxy_type)

    def get_proxy(self):
        if not self.enable:
            return {}
        return getattr(self, self.__proxy_type)()

    @staticmethod
    def socks5_proxy():
        if config.proxy_username:
            socks5 = "{}:{}@{}".format(config.proxy_username, config.proxy_password, config.proxy_ip)
        else:
            socks5 = config.proxy_ip
        proxies = {
            'http': 'socks5://' + socks5,
            'https': 'socks5://' + socks5,
        }
        return proxies


proxy = Proxy()

if __name__ == '__main__':
    print(proxy.get_proxy())
