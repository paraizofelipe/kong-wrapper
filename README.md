kong-wrapper
===============================

version number: 1.0.0
author: Felipe Paraizo

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

#### Server Management
```cmd 

 $ kong-wcli all-confs
 
 $ kong-wcli status
```

#### API Management
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

#### Consumers Management
```cmd
 
 $ kong-wcli consumers add --username '' --custom_id ''
 
 $ kong-wcli consumers list --id [NAME or ID]
 
 $ kong-wcli consumers list
 
 $ kong-wcli consumers update --id [NAME or ID] --username '' --custom_id ''
 
 $ kong-wcli consumers delete --id [NAME or ID]
```

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

#### Certificates Management
```cmd

 $ kong-wcli certs add --cert '' --key '' --snis ''
 
 $ kong-wcli certs list --id [SNI or ID]
 
 $ kong-wcli certs list
 
 $ kong-wcli certs update --id [NAME or ID] --cert '' --key '' --snis ''
 
 $ kong-wcli certs delete --id [NAME or ID]
```

#### SNIs Management
```cmd

 $ kong-wcli snis add --name '' --ssl-certificate-id ''
 
 $ kong-wcli snis list --id [SNI or ID]
 
 $ kong-wcli snis list
 
 $ kong-wcli snis update --id [NAME or ID] --name '' --ssl-certificate-id ''
 
 $ kong-wcli snis delete --id [NAME or ID]
```

####  Upstreams Management
```cmd

 $ kong-wcli upstream add --name '' --slots '' --orderlist ''
 
 $ kong-wcli upstream list --id [SNI or ID]
 
 $ kong-wcli upstream list
 
 $ kong-wcli upstream update --id [NAME or ID] --name '' --slots '' --orderlist ''
 
 $ kong-wcli upstream delete --id [NAME or ID]
```