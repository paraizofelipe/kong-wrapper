import os
import argparse
import configparser

from kong_wrapper.actions import Actions
from kong_wrapper.schemas import Api


class KongCli:

    def __init__(self):
        pass

    def show(self, value):
        print(value)

    def all_confs(self, args):
        try:
            actions = Actions(args.host, args.port)
            self.show(actions.get_all_confs())
        except Exception:
            raise Exception

    def status(self, args):
        try:
            actions = Actions(args.host, args.port)
            self.show(actions.get_status())
        except Exception:
            raise Exception

    def apis(self, args):
        try:
            api = Api()
            actions = Actions(args.host, args.port)

            if args.operation == 'list':
                self.show(actions.get_list_apis(args.list))

            if args.operation == 'add' or args.operation == 'update':
                api.name = args.name
                api.hosts = args.hosts
                api.upstream_url = args.upstream_url
                api.uris = args.uris
                api.methods = args.methods
                api.strip_uri = args.strip_uri
                api.preserve_host = args.preserve_host
                api.retries = args.retries
                api.upstream_connect_timeout = args.upstream_connect_timeout
                api.upstream_send_timeout = args.upstream_send_timeout
                api.upstream_read_timeout = args.upstream_read_timeout
                api.https_only = args.https_only
                api.http_if_terminated = args.http_if_terminated

                if args.operation == 'add':
                    self.show(actions.add_api())
                if args.operation == 'update':
                    self.show(actions.update_api())

        except Exception:
            raise Exception

    def start(self):

        parser = argparse.ArgumentParser(description='CLI ')

        subparser = parser.add_subparsers(help="Commands")

        parser.add_argument("-ht", "--host", required=True, help="Host de acesso ou Kong")
        parser.add_argument("-pt", "--port", required=True, help="Porta de acesso ao host")

        all_config_parser = subparser.add_parser('all-confs', help="Show all configurats of Kong.")
        all_config_parser.set_defaults(func=self.all_confs)

        status_parser = subparser.add_parser('status', help="Mostra o status do serviço kong")
        status_parser.set_defaults(func=self.status)

        apis_parser = subparser.add_parser('apis', help="Mostra informações sobre as APIs cadastradas")
        apis_subparser = apis_parser.add_subparsers(help='commands')

        list_apis_parse = apis_subparser.add_parser('list', help="Lista apis especificas")
        list_apis_parse.set_defaults(func=self.status)

        get_apis_parse = apis_subparser.add_parser('get', help="")
        get_apis_parse.add_argument('--id', required=True, help="")
        get_apis_parse.set_defaults(func=self.status)

        delete_apis_parse = apis_subparser.add_parser('delete', help="")
        delete_apis_parse.add_argument('--id', required=True, help="")
        delete_apis_parse.set_defaults(func=self.status)

        add_apis_parse = apis_subparser.add_parser('add', help="")
        add_apis_parse.add_argument('--name', required=True, help="")
        add_apis_parse.add_argument('--hosts', required=True, help="")
        add_apis_parse.add_argument('--uris', help="")
        add_apis_parse.add_argument('--methods', help="")
        add_apis_parse.add_argument('--upstream_url', help="")
        add_apis_parse.add_argument('--strip_uri', action="store_true", default=True, help="")
        add_apis_parse.add_argument('--preserve_host', action="store_true", default=False, help="")
        add_apis_parse.add_argument('--retries', default=5, help="")
        add_apis_parse.add_argument('--upstream_connect_timeout', default=6000, help="")
        add_apis_parse.add_argument('--upstream_send_timeout', default=6000, help="")
        add_apis_parse.add_argument('--upstream_read_timeout', default=6000, help="")
        add_apis_parse.add_argument('--https_only', default=False, help="")
        add_apis_parse.add_argument('--http_if_terminated', default=False, help="")
        add_apis_parse.set_defaults(func=self.apis)

        update_apis_parse = apis_subparser.add_parser('update', help="")
        update_apis_parse.add_argument('--id', required=True, help="")
        update_apis_parse.add_argument('--name', help="")
        update_apis_parse.add_argument('--hosts', help="")
        update_apis_parse.add_argument('--uris', help="")
        update_apis_parse.add_argument('--methods', help="")
        update_apis_parse.add_argument('--upstream_url', help="")
        update_apis_parse.add_argument('--strip_uri', action="store_true", default=True, help="")
        update_apis_parse.add_argument('--preserve_host', action="store_true", default=False, help="")
        update_apis_parse.add_argument('--retries', default=5, help="")
        update_apis_parse.add_argument('--upstream_connect_timeout', default=6000, help="")
        update_apis_parse.add_argument('--upstream_send_timeout', default=6000, help="")
        update_apis_parse.add_argument('--upstream_read_timeout', default=6000, help="")
        update_apis_parse.add_argument('--https_only', default=False, help="")
        add_apis_parse.set_defaults(func=self.status)

        apis_parser.set_defaults(func=self.apis)

        api = Api()
        args = parser.parse_args(namespace=api)

        try:
            args.func(args)
        except Exception:
            raise Exception


if __name__ == '__main__':
    kongcli = KongCli()
    kongcli.start()
