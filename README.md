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
 
 $ kong-wcli apis list [NAME or ID]
 
 $ kong-wcli apis delete [NAME or ID]
 
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
 
 $ kong-wcli consumers list [NAME or ID]
 
 $ kong-wcli consumers list
 
 $ kong-wcli consumers update [NAME or ID] --username '' --custom_id ''
 
 $ kong-wcli consumers delete [NAME or ID]
```

#### Plugins Management
```cmd

 $ kong-wcli plugins add [NAME or ID] --name '' --consumer_id '' --config ''
 
 $ kong-wcli plugins get [ID]
 
 $ kong-wcli plugins list
 
 $ kong-wcli plugins list api [NAME or ID]
 
 $ kong-wcli plugins update [NAME or ID] --api [NAME or ID]
 
 $ kong-wcli plugins delete [NAME or ID] --api [NAME or ID]
 
 $ kong-wcli plugins enable
 
 $ kong-wcli plugins schema [NAME or ID]
```

#### Certificates Management
```cmd

 $ kong-wcli certificates --cert '' --key '' --snis ''
 
 $ kong-wcli certificates get [SNI or ID]
 
 $ kong-wcli certificates list
 
 $ kong-wcli certificates update [NAME or ID] --cert '' --key '' --snis ''
 
 $ kong-wcli certificates delete [NAME or ID]
```