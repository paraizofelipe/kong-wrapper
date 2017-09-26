import os
import logging
import configparser
import requests


class Kong:

    def __init__(self, conf=None, debug=False):
        self.conf = os.path.abspath(conf or '.')
        self.debu = debug
        self.form_header = {'Content-type': 'application/x-www-form-urlencoded'}

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

    def post(self, path, json=None, data=''):
        url = self.get_api_url(path)
        if json:
            response = requests.post(url, json=json)
        else:
            response = requests.post(url, data=data, headers=self.form_header)
        if response.ok:
            return response

    def delete(self, path):
        url = self.get_api_url(path)
        response = requests.delete(url)
        if response.ok:
            return response