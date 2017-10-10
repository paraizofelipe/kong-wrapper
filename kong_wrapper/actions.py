import json
import requests
from kong_wrapper.schemas import (
    ApiSchema, ComsumerSchema, CertificateSchema, UpstreamSchema, PluginSchema
)


class RequestCRUD:

    def __int__(self, endpoint, schema):
        self.endpoint = endpoint
        self.schema = schema

    def list(self, args):
        try:
            url = 'http://{}:{}/{}/{}'.format(args.host, args.port, self.endpoint, args.id)
            response = requests.get(url)
            return response.json()
        except Exception as error:
            raise error

    def add(self, args):
        try:
            url = 'http://{}:{}/{}'.format(args.host, args.port, self.endpoint)
            dict_result, errors = self.schema.dump(args)
            response = requests.post(url, dict_result)
            return response.json()
        except Exception as error:
            raise error

    def update(self, args):
        try:
            url = 'http://{}:{}/{}/{}'.format(args.host, args.port, self.endpoint, args.id)
            dict_result, errors = self.schema.dump(args)
            response = requests.patch(url, dict_result)
            return response.json()
        except Exception as error:
            raise error

    def delete(self, args):
        try:
            url = 'http://{}:{}/{}/{}'.format(args.host, args.port, self.endpoint, args.id)
            response = requests.delete(url)
            if response.status_code == 404:
                return response.json()
            if response.status_code == 204:
                return {"message": "Deleted"}
        except Exception as error:
            raise error


class ServerActions:
    url = None

    def all_confs(self, args):
        try:
            self.url = 'http://' + args.host + ":" + args.port
            response = requests.get(self.url + '/')
            return response.json()
        except Exception as error:
            raise error

    def status(self, args):
        try:
            self.url = 'http://' + args.host + ":" + args.port
            response = requests.get(self.url + '/status/')
            return response.json()
        except Exception as error:
            raise error


class ApisActions(RequestCRUD):

    def __init__(self):
        self.endpoint = 'apis'
        self.schema = ApiSchema()


class PluginsActions(RequestCRUD):

    def __init__(self):
        super().__init__()
        self.endpoint = 'plugins'
        self.schema = PluginSchema()

    @staticmethod
    def parser_configs(configs):
        dict_config = {}
        for config in configs:
            key = config.split('=')[0]
            value = config.split('=')[1]
            if ',' in value:
                value = value.split(',')
            dict_config[key] = value
        return dict_config

    def add(self, args):
        try:
            session = requests.Session()
            url = 'http://{}:{}/apis/{}/{}'.format(args.host, args.port, args.api_id, self.endpoint)
            args.config = self.parser_configs(args.config)
            plugin, errors = self.schema.dump(args)
            response = session.post(url, json.dumps(plugin), headers={'Content-Type': 'application/json'})
            return response.json()
        except Exception as error:
            raise error

    def delete(self, args):
        try:
            session = requests.Session()
            url = 'http://{}:{}/apis/{}/{}'.format(args.host, args.port, args.api_id, self.endpoint)
            response = session.post(url)
            return response.json()
        except Exception as error:
            raise error

    def update(self, args):
        try:
            session = requests.Session()
            url = 'http://{}:{}/apis/{}/{}/{}'.format(args.host, args.port, args.api_id, self.endpoint, args.id,)
            args.config = self.parser_configs(args.config)
            plugin, errors = self.schema.dump(args)
            import json
            response = session.patch(url, json.dumps(plugin), headers={'Content-Type': 'application/json'})
            return response.json()
        except Exception as error:
            raise error

    def enabled(self, args):
        try:
            url = 'http://{}:{}/{}/enabled'.format(args.host, args.port, self.endpoint)
            response = requests.get(url)
            return response.json()
        except Exception as error:
            raise error

    def get_schema(self, args):
        try:
            url = 'http://{}:{}/{}/schema/{}'.format(args.host, args.port, self.endpoint, args.name)
            response = requests.get(url)
            return response.json()
        except Exception as error:
            raise error


class ComsumersActions(RequestCRUD):

    def __init__(self):
        self.endpoint = 'consumers'
        self.schema = ComsumerSchema()


class CertificatesActions(RequestCRUD):

    def __init__(self):
        self.endpoint = 'certificates'
        self.schema = CertificateSchema()


class SnisActions(RequestCRUD):

    def __init__(self):
        self.endpoint = 'snis'
        self.schema = CertificateSchema()


class UpstreamsActions(RequestCRUD):

    def __init__(self):
        self.endpoint = 'upstreams'
        self.schema = UpstreamSchema()
