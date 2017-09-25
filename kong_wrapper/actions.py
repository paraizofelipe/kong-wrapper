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

    def get_status(self, name_or_id=""):
        try:
            request = requests.get(self.url + '/status/' + name_or_id)
            return request.json()
        except Exception:
            raise Exception

    def get_list_apis(self, id_or_name=''):
        try:
            request = requests.get(self.url + '/apis')
            return request.json()
        except Exception:
            raise Exception
