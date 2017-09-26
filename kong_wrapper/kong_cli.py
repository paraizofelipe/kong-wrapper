import os
import argparse
import configparser

from kong_wrapper.actions import Actions
from kong_wrapper.models.api import Api

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
            actions = Actions(args.host, args.port)
            if args.operation == 'list':
                self.show(actions.get_list_apis(args.list))
            if args.operation == 'add':
                api = Api(args.name, args.hosts, args.upstream_url)
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
                self.show(actions.add_api())

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
        get_apis_parse = apis_subparser.add_parser('get', help="")

        list_apis_parse = apis_subparser.add_parser('list', help="Lista apis especificas")

        add_apis_parse = apis_subparser.add_parser('add', help="")
        name_a = ("--name",)
        name_k = {"help": ""}
        add_apis_parse.add_argument(*name_a, **name_k)
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

        delete_apis_parse = apis_subparser.add_parser('delete', help="")
        delete_apis_parse.add_argument('--name', help="")
        delete_apis_parse.add_argument('--hosts', required=True, help="")
        delete_apis_parse.add_argument('--uris', help="")
        delete_apis_parse.add_argument('--methods', help="")
        delete_apis_parse.add_argument('--upstream_url', help="")
        delete_apis_parse.add_argument('--strip_uri', action="store_true", default=True, help="")
        delete_apis_parse.add_argument('--preserve_host', action="store_true", default=False, help="")
        delete_apis_parse.add_argument('--retries', default=5, help="")
        delete_apis_parse.add_argument('--upstream_connect_timeout', default=6000, help="")
        delete_apis_parse.add_argument('--upstream_send_timeout', default=6000, help="")
        delete_apis_parse.add_argument('--upstream_read_timeout', default=6000, help="")
        delete_apis_parse.add_argument('--https_only', default=False, help="")
        delete_apis_parse.add_argument('--http_if_terminated', default=False, help="")

        delete_apis_parse = apis_subparser.add_parser('update', help="")
        delete_apis_parse.add_argument('--name', help="")
        delete_apis_parse.add_argument('--hosts', required=True, help="")
        delete_apis_parse.add_argument('--uris', help="")
        delete_apis_parse.add_argument('--methods', help="")
        delete_apis_parse.add_argument('--upstream_url', help="")
        delete_apis_parse.add_argument('--strip_uri', action="store_true", default=True, help="")
        delete_apis_parse.add_argument('--preserve_host', action="store_true", default=False, help="")
        delete_apis_parse.add_argument('--retries', default=5, help="")
        delete_apis_parse.add_argument('--upstream_connect_timeout', default=6000, help="")
        delete_apis_parse.add_argument('--upstream_send_timeout', default=6000, help="")
        delete_apis_parse.add_argument('--upstream_read_timeout', default=6000, help="")
        delete_apis_parse.add_argument('--https_only', default=False, help="")

        apis_parser.set_defaults(func=self.apis)

        args = parser.parse_args()

        try:
            args.func(args)
        except Exception:
            raise Exception


if __name__ == '__main__':
    kongcli = KongCli()
    kongcli.start()
