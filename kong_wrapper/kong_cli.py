import argparse
import simplejson as json
from kong_wrapper.utils import read_conf
from pygments import highlight, lexers, formatters
from kong_wrapper.actions import (
    ServerActions, ApisActions, ComsumersActions, CertificatesActions, SnisActions, UpstreamsActions, PluginsActions
)


def show_json(json):
    colorful_json = highlight(json.encode('UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)


def main():

    parser = argparse.ArgumentParser(description='CLI ')

    subparser = parser.add_subparsers(help="Commands")

    parser.add_argument("-ht", "--host", help="Host de acesso ou Kong")
    parser.add_argument("-pt", "--port", help="Porta de acesso ao host")

    all_config_parser = subparser.add_parser('all-confs', help="Show all configurats of Kong.")
    all_config_parser.set_defaults(func=ServerActions().all_confs)

    status_parser = subparser.add_parser('status', help="Mostra o status do serviço Kong.")
    status_parser.set_defaults(func=ServerActions().status)

    # ----APIS----

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

    # ----COMSUMERS----

    consumers_parser = subparser.add_parser('consumers', help="")
    consumers_subparser = consumers_parser.add_subparsers(help='commands')

    list_consumers_parse = consumers_subparser.add_parser('list', help="")
    list_consumers_parse.add_argument('--id', default='', help="")
    list_consumers_parse.set_defaults(func=ComsumersActions().list)

    delete_consumers_parse = consumers_subparser.add_parser('delete', help="")
    delete_consumers_parse.add_argument('--id', required=True, help="")
    delete_consumers_parse.set_defaults(func=ComsumersActions().delete)

    add_consumers_parse = consumers_subparser.add_parser('add', help="")
    add_consumers_parse.add_argument('--username', help="")
    add_consumers_parse.add_argument('--custom_id', help="")
    add_consumers_parse.set_defaults(func=ComsumersActions().add)

    update_consumers_parse = consumers_subparser.add_parser('update', help="")
    update_consumers_parse.add_argument('--username', help="")
    update_consumers_parse.add_argument('--custom_id', help="")
    update_consumers_parse.set_defaults(func=ComsumersActions().update)

    # ----PLUGINS----

    plugins_parser = subparser.add_parser('plugins', help="")
    plugins_subparser = plugins_parser.add_subparsers(help='commands')

    list_plugins_parse = plugins_subparser.add_parser('list', help="")
    list_plugins_parse.add_argument('--id', default='', help="")
    list_plugins_parse.set_defaults(func=PluginsActions().list)

    enabled_plugins_parse = plugins_subparser.add_parser('enabled', help="")
    enabled_plugins_parse.set_defaults(func=PluginsActions().enabled)

    schema_plugins_parse = plugins_subparser.add_parser('schema', help="")
    schema_plugins_parse.add_argument('--name', required=True, help="")
    schema_plugins_parse.set_defaults(func=PluginsActions().get_schema)

    add_plugins_parse = plugins_subparser.add_parser('add', help="")
    add_plugins_parse.add_argument('--api-id', required=True, default='', help="")
    add_plugins_parse.add_argument('--name', required=True, help="")
    add_plugins_parse.add_argument('--consumer-id', help="")
    add_plugins_parse.add_argument('--config', '-c', required=True, action='append', dest='config', help="")
    add_plugins_parse.set_defaults(func=PluginsActions().add)

    update_plugins_parse = plugins_subparser.add_parser('update', help="")
    update_plugins_parse.add_argument('--id', required=True, help="")
    update_plugins_parse.add_argument('--api-id', required=True, default='', help="")
    update_plugins_parse.add_argument('--name', required=True, help="")
    update_plugins_parse.add_argument('--consumer-id', help="")
    update_plugins_parse.add_argument('--config', '-c', required=True, action='append', dest='config', help="")
    update_plugins_parse.set_defaults(func=PluginsActions().update)

    # ----CERTIFICATES----

    certificates_parser = subparser.add_parser('cert', help="")
    certificates_subparser = certificates_parser.add_subparsers(help='commands')

    list_certificates_parse = certificates_subparser.add_parser('list', help="")
    list_certificates_parse.add_argument('--id', default='', help="")
    list_certificates_parse.set_defaults(func=CertificatesActions().list)

    delete_certificates_parse = certificates_subparser.add_parser('delete', help="")
    delete_certificates_parse.add_argument('--id', required=True, help="")
    delete_certificates_parse.set_defaults(func=CertificatesActions().delete)

    add_certificates_parse = certificates_subparser.add_parser('add', help="")
    add_certificates_parse.add_argument('--cert', required=True, help="")
    add_certificates_parse.add_argument('--key', required=True, help="")
    add_certificates_parse.add_argument('--snis', help="")
    add_certificates_parse.set_defaults(func=CertificatesActions().add)

    update_certificates_parse = certificates_subparser.add_parser('update', help="")
    update_certificates_parse.add_argument('--cert', required=True, help="")
    update_certificates_parse.add_argument('--key', required=True, help="")
    update_certificates_parse.add_argument('--snis', help="")
    update_certificates_parse.set_defaults(func=CertificatesActions().update)

    # ----SNI----

    sni_parser = subparser.add_parser('sni', help="")
    sni_subparser = sni_parser.add_subparsers(help='commands')

    list_sni_parse = sni_subparser.add_parser('list', help="")
    list_sni_parse.add_argument('--id', default='', help="")
    list_sni_parse.set_defaults(func=CertificatesActions().list)

    delete_sni_parse = certificates_subparser.add_parser('delete', help="")
    delete_sni_parse.add_argument('--id', required=True, help="")
    delete_sni_parse.set_defaults(func=CertificatesActions().delete)

    add_sni_parse = sni_subparser.add_parser('add', help="")
    add_sni_parse.add_argument('--name', help="")
    add_sni_parse.add_argument('--ssl-certificate-id', help="")
    add_sni_parse.set_defaults(func=SnisActions().add)

    update_sni_parse = sni_subparser.add_parser('update', help="")
    update_sni_parse.add_argument('--name', help="")
    update_sni_parse.add_argument('--ssl-certificate-id', help="")
    update_sni_parse.set_defaults(func=SnisActions().update)

    # ----UPSTREAM----

    upstream_parser = subparser.add_parser('upstream', help="")
    upstream_subparser = upstream_parser.add_subparsers(help='commands')

    list_upstream_parse = upstream_subparser.add_parser('list', help="")
    list_upstream_parse.add_argument('--id', default='', help="")
    list_upstream_parse.set_defaults(func=UpstreamsActions().list)

    delete_upstream_parse = certificates_subparser.add_parser('delete', help="")
    delete_upstream_parse.add_argument('--id', required=True, help="")
    delete_upstream_parse.set_defaults(func=CertificatesActions().delete)

    add_upstream_parse = upstream_subparser.add_parser('add', help="")
    add_upstream_parse.add_argument('--name', required=True, help="")
    add_upstream_parse.add_argument('--slots', help="")
    add_upstream_parse.add_argument('--orderlist', help="")
    add_upstream_parse.set_defaults(func=UpstreamsActions().add)

    update_upstream_parse = upstream_subparser.add_parser('update', help="")
    update_upstream_parse.add_argument('--name', required=True, help="")
    update_upstream_parse.add_argument('--slots', help="")
    update_upstream_parse.add_argument('--orderlist', help="")
    update_upstream_parse.set_defaults(func=UpstreamsActions().update)

    args = parser.parse_args()

    try:
        cli_conf = read_conf('default')
        if not args.host or not args.port:
            if cli_conf and cli_conf["host"] and cli_conf["port"]:
                args.host = cli_conf["host"]
                args.port = cli_conf["port"]

                try:
                    result_request = args.func(args)
                    result_request = json.dumps(result_request, sort_keys=True, indent=True)
                    # print(result_request)
                    show_json(result_request)
                except Exception as error:
                    raise error

            else:
                raise argparse.ArgumentError(subparser, "host and port values have not been defined.")
    except FileNotFoundError:
        print('The file ".kong" not found in directory "home" of user!')
    except Exception as error:
        raise error


if __name__ == '__main__':
    main()
