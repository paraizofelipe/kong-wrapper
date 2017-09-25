import os
import argparse
import configparser

from kong_wrapper.actions import Actions


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
            if args.list:
                self.show(actions.get_list_apis(args.list))
            if args.create:
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
        apis_parser.add_argument('--list', action="store_true", default=False, help='Lista apis especificas')
        apis_parser.add_argument('--get', dest='name_or_id', help="Lista apis especificas")
        x = apis_parser.add_argument('create', action="store_true", default=False, help='Adiciona uma api ao kong.')
        apis_parser.add_argument('--name', help="Nome da API a ser adicionada.")
        apis_parser.add_argument('--hosts', help="Hosts da APi a ser adicionada.")
        apis_parser.add_argument('--methods', help="Lista de metodos de acesso a API.")
        apis_parser.add_argument('--upstream_url', help="Upstream de acesso a API.")

        apis_parser.set_defaults(func=self.apis)

        args = parser.parse_args()

        try:
            args.func(args)
        except Exception:
            raise Exception


if __name__ == '__main__':
    kongcli = KongCli()
    kongcli.start()
