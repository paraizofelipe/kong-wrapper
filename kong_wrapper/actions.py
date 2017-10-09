import requests
from kong_wrapper.schemas import ApiSchema, ComsumersSchema


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
            return response.json()
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


class ComsumersActions(RequestCRUD):

    def __init__(self):
        self.endpoint = 'consumers'
        self.schema = ComsumersSchema()
