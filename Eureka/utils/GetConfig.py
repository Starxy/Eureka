import os
from configparser import ConfigParser


class GetConfig(object):

    def __init__(self):
        self.pwd = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.config_path = os.path.join(self.pwd, 'config.ini')
        self.config_file = ConfigParser()
        self.config_file.read(self.config_path)

    def db_host(self):
        return self.config_file.get('db', 'host')

    def db_port(self):
        return self.config_file.get('db', 'port')

    def db_name(self):
        return self.config_file.get('db', 'name')

    def api_host(self):
        return self.config_file.get('API', 'host')

    def api_port(self):
        return self.config_file.get('API', 'port')

    def socks5_enable(self):
        return self.config_file.get('socks5', 'enable')

    def socks5_ip(self):
        return self.config_file.get('socks5', 'ip')

    def socks5_username(self):
        return self.config_file.get('socks5', 'username')

    def socks5_password(self):
        return self.config_file.get('socks5', 'password')


config = GetConfig()

if __name__ == '__main__':
    gg = GetConfig()
    print(int(gg.db_port()))
