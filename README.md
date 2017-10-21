<img src="https://orig00.deviantart.net/b694/f/2013/018/0/5/1donkeykong_by_camdencc-d5rwxvz.gif" width="115px" align="left"/>

KONG Wrapper CLI
===============================
<br>
* version number: 1.0.0
* author: Felipe Paraizo

Overview
--------

CLI to facilitate the management of APIs with Kong

Installation / Usage
--------------------

To install use pip:

    $ pip install kong_wrapper


Or clone the repo:

    $ git clone https://github.com/paraizofelipe/kong-wrapper.git
    $ python setup.py install
    
Contributing
------------

TBD

Example
------

TBD

Commands
-------

### Server Management
```cmd 

 $ kong-wcli all-confs
 
 $ kong-wcli status
```

### API Management
```cmd
 
 $ kong-wcli apis list
 
 $ kong-wcli apis list --id [NAME or ID]
 
 $ kong-wcli apis delete --id [NAME or ID]
 
 $ kong-wcli apis add --name [NAME] \
  --hosts HOSTS \
  --uris URIS \
  --methods METHODS \
  --upstream_url UPSTREAM_URL \
  --strip_uri \
  --preserve_host \
  --retries RETRIES \
  --upstream_connect_timeout UPSTREAM_CONNECT_TIMEOUT \
  --upstream_send_timeout UPSTREAM_SEND_TIMEOUT \
  --upstream_read_timeout UPSTREAM_READ_TIMEOUT \
  --https_only HTTPS_ONLY \
  --http_if_terminated HTTP_IF_TERMINATED
    
 $ kong-wcli apis update --name '' \
  --hosts HOSTS \
  --uris URIS \
  --methods METHODS \
  --upstream_url UPSTREAM_URL \
  --strip_uri \
  --preserve_host \
  --retries RETRIES \
  --upstream_connect_timeout UPSTREAM_CONNECT_TIMEOUT \
  --upstream_send_timeout UPSTREAM_SEND_TIMEOUT \
  --upstream_read_timeout UPSTREAM_READ_TIMEOUT \
  --https_only HTTPS_ONLY \
  --http_if_terminated HTTP_IF_TERMINATED
 
```
#### Description of parameters

The API paramters describes an API that’s being exposed by Kong. Kong needs to know how to retrieve the API when a consumer is calling it from the Proxy port. Each API object must specify some combination of hosts, uris, and methods. Kong will proxy all requests to the API to the specified upstream URL.


* `--name`: The API name.

* `--hosts`: A comma-separated list of domain names that point to your API. For example: example.com. At least one of hosts, uris, or methods should be specified.

* `--uris`: A comma-separated list of URIs prefixes that point to your API. For example: /my-path. At least one of hosts, uris, or methods should be specified.

* `--methods`: A comma-separated list of HTTP methods that point to your API. For example: GET,POST. At least one of hosts, uris, or methods should be specified.

* `--upstream_url`: The base target URL that points to your API server. This URL will be used for proxying requests. For example: https://example.com.

* `--strip_uri`: When matching an API via one of the uris prefixes, strip that matching prefix from the upstream URI to be requested. Default: true.

* `--preserve_host`: When matching an API via one of the hosts domain names, make sure the request Host header is forwarded to the upstream service. By default, this is false, and the upstream Host header will be extracted from the configured upstream_url.

* `--retries`: The number of retries to execute upon failure to proxy. The default is 5.

* `--upstream_connect_timeout`: The timeout in milliseconds for establishing a connection to your upstream service. Defaults to 60000.

* `--upstream_send_timeout`: The timeout in milliseconds between two successive write operations for transmitting a request to your upstream service Defaults to 60000.

* `--upstream_send_timeout`: The timeout in milliseconds between two successive read operations for transmitting a request to your upstream service Defaults to 60000.

* `--https_only`: To be enabled if you wish to only serve an API through HTTPS, on the appropriate port (8443 by default). Default: false.

* `--http_if_terminated`: Consider the X-Forwarded-Proto header when enforcing HTTPS only traffic. Default: true.

#### Consumers Management
```cmd
 
 $ kong-wcli consumers add --username '' --custom_id ''
 
 $ kong-wcli consumers list --id [NAME or ID]
 
 $ kong-wcli consumers list
 
 $ kong-wcli consumers update --id [NAME or ID] --username '' --custom_id ''
 
 $ kong-wcli consumers delete --id [NAME or ID]
```

#### Description of parameters

* `--id`: The unique identifier or the username of the consumer to retrieve.
* `--username`: The unique username of the consumer. You must send either this field or custom_id with the request.
* `--custom_id`: Field for storing an existing unique ID for the consumer - useful for mapping Kong with users in your existing database. You must send either this field or username with the request.

#### Plugins Management
```cmd

 $ kong-wcli plugins add [NAME or ID] --name '' --consumer_id '' --config ''
 
 $ kong-wcli plugins list [ID]
 
 $ kong-wcli plugins list
 
 $ kong-wcli plugins list api [NAME or ID]
 
 $ kong-wcli plugins update [NAME or ID] --api [NAME or ID]
 
 $ kong-wcli plugins delete [NAME or ID] --api [NAME or ID]
 
 $ kong-wcli plugins enable
 
 $ kong-wcli plugins schema [NAME or ID]
```

#### Description of parameters

A Plugin entity represents a plugin configuration that will be executed during the HTTP request/response workflow, and it's how you can add functionalities to APIs that run behind Kong, like Authentication or Rate Limiting for example. You can find more information about how to install and what values each plugin takes by visiting the Plugin Gallery.

When creating adding Plugin on top of an API, every request made by a client will be evaluated by the Plugin's configuration you setup. Sometimes the Plugin needs to be tuned to different values for some specific consumers, you can do that by specifying the consumer_id value.

* `--id` The unique identifier of the plugin to retrieve.

* `--name`: The name of the Plugin that's going to be added. Currently the Plugin must be installed in every Kong instance separately.

* `--consumer_id`: The unique identifier of the consumer that overrides the existing settings for this specific consumer on incoming requests.

* `--config`: The configuration properties for the Plugin which can be found on the plugins documentation page in the Plugin Gallery.

* `--api`: A filter on the list based on the api_id field.

#### Certificates Management
```cmd

 $ kong-wcli certs add --cert '' --key '' --snis ''
 
 $ kong-wcli certs list --id [SNI or ID]
 
 $ kong-wcli certs list
 
 $ kong-wcli certs update --id [NAME or ID] --cert '' --key '' --snis ''
 
 $ kong-wcli certs delete --id [NAME or ID]
```
#### Description of parameters

The paramters represents a public certificate/private key pair for an SSL certificate. These paramters are used by Kong to handle SSL/TLS termination for encrypted requests. Certificates are optionally associated with SNI objects to tie a cert/key pair to one or more hostnames.

* `--id`: 

* `--cert`: PEM-encoded public certificate of the SSL key pair.

* `--key`: PEM-encoded private key of the SSL key pair.

* `--snis`: One or more hostnames to associate with this certificate as an SNI. This is a sugar parameter that will, under the hood, create an SNI object and associate it with this certificate for your convenience.

#### SNIs Management
```cmd

 $ kong-wcli snis add --name '' --ssl-certificate-id ''
 
 $ kong-wcli snis list --id [SNI or ID]
 
 $ kong-wcli snis list
 
 $ kong-wcli snis update --id [NAME or ID] --name '' --ssl-certificate-id ''
 
 $ kong-wcli snis delete --id [NAME or ID]
```

An SNI object represents a many-to-one mapping of hostnames to a certificate. That is, a certificate object can have many hostnames associated with it; when Kong receives an SSL request, it uses the SNI field in the Client Hello to lookup the certificate object based on the SNI associated with the certificate.

#### Description of parameters

* `--name`: The SNI name to associate with the given certificate.
 
* `--ssl-certificate-id`: The id (a UUID) of the certificate with which to associate the SNI hostname.

* `--id`: 
 
####  Upstreams Management
```cmd

 $ kong-wcli upstream add --name '' --slots '' --orderlist ''
 
 $ kong-wcli upstream list --id [SNI or ID]
 
 $ kong-wcli upstream list
 
 $ kong-wcli upstream update --id [NAME or ID] --name '' --slots '' --orderlist ''
 
 $ kong-wcli upstream delete --id [NAME or ID]
```
