import argparse
import simplejson as json
from kong_wrapper.actions import ServerActions, ApisActions, ComsumersActions


class KongCli:

    def __init__(self):
        pass

    def start(self):

        parser = argparse.ArgumentParser(description='CLI ')

        subparser = parser.add_subparsers(help="Commands")

        parser.add_argument("-ht", "--host", required=True, help="Host de acesso ou Kong")
        parser.add_argument("-pt", "--port", required=True, help="Porta de acesso ao host")

        all_config_parser = subparser.add_parser('all-confs', help="Show all configurats of Kong.")
        all_config_parser.set_defaults(func=ServerActions().all_confs)

        status_parser = subparser.add_parser('status', help="Mostra o status do serviço Kong.")
        status_parser.set_defaults(func=ServerActions().status)

        # APIS

        apis_parser = subparser.add_parser('apis', help="Mostra informações sobre as APIs cadastradas")
        apis_subparser = apis_parser.add_subparsers(help='commands')

        list_apis_parse = apis_subparser.add_parser('list', help="Lista apis especificas")
        list_apis_parse.add_argument('--id', default='', help="")
        list_apis_parse.set_defaults(func=ApisActions().list)

        delete_apis_parse = apis_subparser.add_parser('delete', help="")
        delete_apis_parse.add_argument('--id', required=True, help="")
        delete_apis_parse.set_defaults(func=ApisActions().delete)

        add_apis_parse = apis_subparser.add_parser('add', help="")
        add_apis_parse.add_argument('--name', required=True, help="")
        add_apis_parse.add_argument('--hosts', required=True, help="")
        add_apis_parse.add_argument('--uris', help="")
        add_apis_parse.add_argument('--methods', help="")
        add_apis_parse.add_argument('--upstream_url', required=True, help="")
        add_apis_parse.add_argument('--strip_uri', action="store_true", default=True, help="")
        add_apis_parse.add_argument('--preserve_host', action="store_true", default=False, help="")
        add_apis_parse.add_argument('--retries', default=5, help="")
        add_apis_parse.add_argument('--upstream_connect_timeout', default=6000, help="")
        add_apis_parse.add_argument('--upstream_send_timeout', default=6000, help="")
        add_apis_parse.add_argument('--upstream_read_timeout', default=6000, help="")
        add_apis_parse.add_argument('--https_only', default=False, help="")
        add_apis_parse.add_argument('--http_if_terminated', default=False, help="")
        add_apis_parse.set_defaults(func=ApisActions().add)

        update_apis_parse = apis_subparser.add_parser('update', help="")
        update_apis_parse.add_argument('--id', required=True, help="")
        update_apis_parse.add_argument('--name', help="")
        update_apis_parse.add_argument('--hosts', help="")
        update_apis_parse.add_argument('--uris', help="")
        update_apis_parse.add_argument('--methods', help="")
        update_apis_parse.add_argument('--upstream_url', required=True, help="")
        update_apis_parse.add_argument('--strip_uri', action="store_true", default=True, help="")
        update_apis_parse.add_argument('--preserve_host', action="store_true", default=False, help="")
        update_apis_parse.add_argument('--retries', default=5, help="")
        update_apis_parse.add_argument('--upstream_connect_timeout', default=6000, help="")
        update_apis_parse.add_argument('--upstream_send_timeout', default=6000, help="")
        update_apis_parse.add_argument('--upstream_read_timeout', default=6000, help="")
        update_apis_parse.add_argument('--https_only', default=False, help="")
        update_apis_parse.set_defaults(func=ApisActions().update)

        # COMSUMERS

        consumers_parser = subparser.add_parser('consumers', help="")
        consumers_subparser = consumers_parser.add_subparsers(help='commands')

        list_consumers_parse = consumers_subparser.add_parser('list', help="")
        list_consumers_parse.add_argument('--id', default='', help="")
        list_consumers_parse.set_defaults(func=ComsumersActions().list)

        delete_consumers_parse = consumers_subparser.add_parser('delete', help="")
        delete_consumers_parse.add_argument('--id', required=True, help="")
        delete_consumers_parse.set_defaults(func=ComsumersActions().delete)

        add_consumers_parse = consumers_subparser.add_parser('add', help="")
        add_consumers_parse.add_argument('--username', required=True, help="")
        add_consumers_parse.add_argument('--custom_id', required=True, help="")
        add_consumers_parse.set_defaults(func=ComsumersActions().add)

        update_consumers_parse = consumers_subparser.add_parser('update', help="")
        update_consumers_parse.add_argument('--username', required=True, help="")
        update_consumers_parse.add_argument('--custom_id', required=True, help="")
        update_consumers_parse.set_defaults(func=ComsumersActions().update)

        # PLUGINS

        plugins_parser = subparser.add_parser('plugins', help="")
        plugins_subparser = plugins_parser.add_subparsers(help='commands')

        list_plugins_parse = plugins_subparser.add_parser('list', help="")
        list_plugins_parse.add_argument('--id', default='', help="")
        # list_plugins_parse.set_defaults(func=PluginsActions().list)

        args = parser.parse_args()

        try:
            result_request = args.func(args)
            result_request = json.dumps(result_request, sort_keys=True, indent=True)
            print(result_request)
        except Exception as error:
            raise error


if __name__ == '__main__':
    kongcli = KongCli()
    kongcli.start()
