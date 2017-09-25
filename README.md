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
```cmd 

 $ kong-wcli all-confs
 
 $ kong-wcli status
 
 $ kong-wcli apis --list
 
 $ kong-wcli apis --action list [NAME or ID]
 
 $ kong-wcli apis --action add --name '' \
    --hosts '' \
    --uris '' \
    --methods '' \
    --upstream_url '' \
    --strip_uri '' \
    --preserve_host '' \
    --retries '' \
    --upstream_connect_timeout '' \
    --upstream_send_timeout '' \
    --upstream_read_timeout '' \
    --https_only '' \
    --http_if_terminated ''
    
 $ kong-wcli apis --action update --name '' \
    --hosts '' \
    --uris '' \
    --methods '' \
    --upstream_url '' \
    --strip_uri '' \
    --preserve_host '' \
    --retries '' \
    --upstream_connect_timeout '' \
    --upstream_send_timeout '' \
    --upstream_read_timeout '' \
    --https_only '' \
    --http_if_terminated '' \
    
 $ kong-wcli apis --delete [NAME or ID]
 
 $ kong-wcli consumers --create --username '' --custom_id ''
 
 $ kong-wcli consumers --retrive [NAME or ID]
 
 $ kong-wcli consumers --list
 
 $ kong-wcli consumers --update [NAME or ID] --username '' --custom_id ''
 
 $ kong-wcli consumers --delete [NAME or ID]
 
 $ kong-wcli plugins --add [NAME or ID] --name '' --consumer_id '' --config ''
 
 $ kong-wcli plugins --retrive [ID]
 
 $ kong-wcli plugins --list
 
 $ kong-wcli plugins --list --api [NAME or ID]
 
 $ kong-wcli plugins --update [NAME or ID] --api [NAME or ID]
 
 $ kong-wcli plugins --delete [NAME or ID] --api [NAME or ID]
 
 $ kong-wcli plugins --retrive --enable
 
 $ kong-wcli plugins --schema [NAME or ID]
 
 $ kong-wcli certificates --cert '' --key '' --snis ''
 
 $ kong-wcli certificates --retrive [SNI or ID]
 
 $ kong-wcli certificates --list
 
 $ kong-wcli certificates --update [NAME or ID] --cert '' --key '' --snis ''
 
 $ kong-wcli certificates --delete [NAME or ID]
```

