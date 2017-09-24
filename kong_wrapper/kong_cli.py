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
            self.show(actions.get_apis())
        except Exception:
            raise Exception

    def start(self):

        parser = argparse.ArgumentParser(description='CLI ')

        subparser = parser.add_subparsers(help="Commands")

        # host_params = {"option_strings": "-ht", "dest": "--host", "help": "Host de acesso ao kong"}
        # port_params = {"option_strings": "-pt", "dest": "--port", "help": "Porta de acesso ao host"}

        all_config_parser = subparser.add_parser('all-confs', help="Show all configurats of Kong.")
        all_config_parser.add_argument("-ht", "--host", help="Host de acesso ou Kong")
        all_config_parser.add_argument("-pt", "--port", help="Porta de acesso ao host")
        all_config_parser.set_defaults(func=self.all_confs)

        status_parser = subparser.add_parser('status', help="Mostra o status do serviço kong")
        status_parser.add_argument("-ht", "--host", help="Host de acesso ou Kong")
        status_parser.add_argument("-pt", "--port", help="Porta de acesso ao host")
        status_parser.set_defaults(func=self.status)

        apis_parser = subparser.add_parser('apis', help="Mostra informações sobre as APIs cadastradas")
        apis_parser.add_argument("-ht", "--host", help="Host de acesso ou Kong")
        apis_parser.add_argument("-pt", "--port", help="Porta de acesso ao host")
        apis_parser.add_argument('list', help="Lista apis especificas")
        apis_parser.add_argument('create', help="Cria uma API especificas")
        apis_parser.add_argument('--hosts', help="Teste")

        apis_parser.set_defaults(func=self.apis)

        args = parser.parse_args()

        try:
            args.func(args)
        except Exception:
            raise Exception


if __name__ == '__main__':
    kongcli = KongCli()
    kongcli.start()
