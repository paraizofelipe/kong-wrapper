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
            api, errors = self.schema.dump(args)
            response = requests.post(url, api)
            return response.json()
        except Exception as error:
            raise error

    def update(self, args):
        try:
            url = 'http://{}:{}/{}/{}'.format(args.host, args.port, self.endpoint, args.id)
            api, errors = self.schema.dump(args)
            response = requests.patch(url, api)
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

    def add_plugin(self, args):
        try:
            url = 'http://{}:{}/{}/plugins'.format(args.host, args.port, self.endpoint)
            plugin, errors = self.schema.dump(args)
            response = requests.post(url, plugin)
            return response.json()
        except Exception as error:
            raise error

    def list_plugin(self, args):
        try:
            url = 'http://{}:{}/{}/plugins'.format(args.host, args.port, self.endpoint)
            response = requests.get(url)
            return response.json()
        except Exception as error:
            raise error

    def update_plugin(self, args):
        try:
            url = 'http://{}:{}/{}/plugins/{}'.format(args.host, args.port, self.endpoint, args.id)
            plugin, errors = self.schema.dump(args)
            response = requests.patch(url, plugin)
            return response.json()
        except Exception as error:
            raise error

    def delete_plugin(self, args):
        try:
            url = 'http://{}:{}/{}/plugins/{}'.format(args.host, args.port, self.endpoint, args.id)
            response = requests.delete(url)
            return response.json()
        except Exception as error:
            raise error


class PluginsActions(ApisActions):

    def __init__(self):
        super().__init__()
        self.endpoint = 'plugins'
        self.schema = PluginSchema()

    def add(self, args):
        pass

    def delete(self, args):
        pass

    def update(self, args):
        pass

    def enabled(self, args):
        try:
            url = 'http://{}:{}/{}/enabled'.format(args.host, args.port, self.endpoint)
            response = requests.get(url)
            return response.json()
        except Exception as error:
            raise error

    def schema(self, args):
        try:
            url = 'http://{}:{}/{}/schema/{}'.format(args.host, args.port, self.endpoint, args.id)
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
