import os
from configparser import ConfigParser
from Eureka.Utils.utilClass import LazyProperty


class GetConfig(object):
    """
    从项目根目录下 config.ini 文件中读取配置信息
    """

    def __init__(self):
        self.pwd = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.config_path = os.path.join(self.pwd, 'config.ini')
        self.config_file = ConfigParser()
        self.config_file.read(self.config_path, encoding="UTF-8")

    @LazyProperty
    def db_host(self):
        return self.config_file.get('DB', 'host')

    @LazyProperty
    def db_port(self):
        return self.config_file.get('DB', 'port')

    @LazyProperty
    def db_name(self):
        return self.config_file.get('DB', 'name')\

    @LazyProperty
    def db_type(self):
        return self.config_file.get('DB', 'type')

    @LazyProperty
    def db_username(self):
        return self.config_file.get('DB', 'username')

    @LazyProperty
    def db_password(self):
        return self.config_file.get('DB', 'password')

    @LazyProperty
    def api_host(self):
        return self.config_file.get('API', 'host')

    @LazyProperty
    def api_port(self):
        return self.config_file.get('API', 'port')

    @LazyProperty
    def proxy_enable(self):
        return self.config_file.get('Proxy', 'enable')

    @LazyProperty
    def proxy_type(self):
        return self.config_file.get('Proxy', 'type')

    @LazyProperty
    def proxy_ip(self):
        return self.config_file.get('Proxy', 'ip')

    @LazyProperty
    def proxy_username(self):
        return self.config_file.get('Proxy', 'username')

    @LazyProperty
    def proxy_password(self):
        return self.config_file.get('Proxy', 'password')


config = GetConfig()

if __name__ == '__main__':
    gg = GetConfig()
    print(int(gg.db_port()))
