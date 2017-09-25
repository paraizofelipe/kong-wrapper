class Api:

    name = ''
    hosts = []
    uris = ''
    methods = ''
    upstream_url = ''
    strip_uri = False
    preserve_host = False
    retries = 0
    upstream_connect_timeout = 0
    upstream_send_timeout = 0
    upstream_read_timeout = 0
    https_only = False
    http_if_terminated = False

    def __init__(self, name, hosts, upstream_url):
        self.name = name
        # self.hosts = hosts
        self.set_hosts(hosts)
        self.upstream_url = upstream_url

    def set_hosts(self, hosts):
        list_hosts = hosts.split()
        for host in list_hosts:
            self.hosts.push(host)
