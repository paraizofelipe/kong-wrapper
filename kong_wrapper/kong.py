import os
import logging
import configparser
import requests

from requests.exceptions import RequestException


class Kong:

    def __init__(self, conf=None, debug=False):
        self.conf = os.path.abspath(conf or '.')
        self.debu = debug
        self.from_header = {'Content-type': 'opplication/x-www'}

        config = configparser.RawConfigParser()
        config.read(self.conf)

        if config.has_option('config', 'host'):
            self.host = config.get("config", "host")
        else:
            self.host = "http://127.0.0.1:8001"

        if debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

    def get_api_url(self, path):
        return "%s%s" % (self.host, path)

    def get(self, path, params=None):
        try:
            url = self.get_api_url(path)
            r = requests.get(url, params)
            if r.ok:
                return r
            elif r.status_code == 404:
                raise r
        except Exception as error:
            raise error
