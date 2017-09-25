import os
import click
import simplejson as json

from kong_wrapper.kong import Kong


def parse_json(obj):
    return json.dumps(obj, sort_keys=True, indent=2 * ' ')


def cleanup_params(data, empty_string=False):
    for k, v in list(data.items()):
        if not isinstance(v, (str, int)) or (empty_string and v == ""):
            data.pop(k)
    data.pop('kong', None)
    return data


@click.group(help="CLI wrapper from Kong")
@click.option("--conf", default=os.path.expanduser("~/.kong_wrapper"))
@click.pass_context
def cli(ctx, conf):
    ctx.obj = Kong(conf)


@cli.command()
@click.pass_obj
def status(kong):
    try:
        response = kong.get("/status")
        print(parse_json(response.json()))
    except Exception as error:
        raise error


@cli.group()
@click.pass_obj
def apis(kong):
    pass


@apis.command("list")
@click.option('--id', help="a filter on the list based on the api `id` field")
@click.option('--name', help="a filter on the list based on the api `name` field")
@click.option('--upstream-url', help="a filter on the list based on the api `upstream_url` field")
@click.option('--retries', help="a filter on the list based on the api `retries` field")
@click.option('--size', help="a filter on the list based on the api `size` field")
@click.option('--offset', help="a filter on the list based on the api `offset` field")
@click.pass_obj
def api_list(kong, id, name, upstream_url, retries, size, offset):
    params = cleanup_params(vars())
    response = kong.get("/apis/", params=params)
    print(parse_json(response.json()))


@apis.command("get")
@click.argument('name')
@click.pass_obj
def api_get(kong, name):
    try:
        params = cleanup_params(vars())
        response = kong.get("/apis/%s" % name)
        print(parse_json(response.json()))
    except Exception as error:
        raise error


@apis.command("add")
@click.argument('name')
@click.option('--hosts', prompt='hosts', default="example.com", help="A comma-separated list of domain names that point to your API")
@click.option('--uris', prompt='uris', default="", help="A comma-separated list of URIs prefixes that point to your API.")
@click.option('--methods', prompt='methods', default="GET,PUT,POST,DELETE", help="A comma-separated list of HTTP methods that point to your API.")
@click.option('--upstream-url', prompt='upstream url', default="https://example.com", help="The base target URL that points to your API server. ")
@click.option('--strip-uri', help="When matching an API via one of the uris prefixes, strip that matching prefix from the upstream URI to be requested. ")
@click.option('--preserve-host', help="When matching an API via one of the hosts domain names, make sure the request Host header is forwarded to the upstream service.")
@click.option('--retries', help="The number of retries to execute upon failure to proxy. ")
@click.option('--upstream-connect-timeout', help="The timeout in milliseconds for establishing a connection to your upstream service. ")
@click.option('--upstream-send-timeout', help="The timeout in milliseconds between two successive write operations for transmitting a request to your upstream service")
@click.option('--upstream-read-timeout', help="The timeout in milliseconds between two successive read operations for transmitting a request to your upstream service")
@click.option('--https-only', help="To be enabled if you wish to only serve an API through HTTPS")
@click.option('--http-if-terminated', help="Consider the X-Forwarded-Proto header when enforcing HTTPS only traffic")
@click.pass_obj
def api_add(kong, name, hosts, uris, methods, upstream_url, strip_uri, preserve_host, retries,
    upstream_connect_timeout, upstream_send_timeout, upstream_read_timeout, https_only,
    http_if_terminated):
    data = cleanup_params(vars(), True)
    response = kong.post("/apis/", data=data)
    print(parse_json(response))


if __name__ == "__main__":
    cli()
