#!/bin/bash
cfg="config.ini"
echo "Using configuration file: $cfg"
pipenv run python xmpp_send.py -c $cfg
