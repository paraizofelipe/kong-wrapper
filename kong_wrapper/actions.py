import requests


class Actions:

    def __init__(self, host, port, protocol='http'):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.url = protocol + '://' + host + ':' + port

    def get_all_confs(self):
        try:
            request = requests.get(self.url)
            return request.json()
        except Exception:
            raise Exception

    def get_status(self):
        try:
            request = requests.get(self.url + '/status')
            return request.json()
        except Exception:
            raise Exception

    def get_apis(self):
        try:
            request = requests.get(self.url + '/apis')
            return request.json()
        except Exception:
            raise Exception
