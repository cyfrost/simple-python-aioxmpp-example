#!/bin/sh
key="$1"
value="$2"
configfile="$3"
sed -i 's|^'"$key"' = .*|'"$key"' = '"$value"' |g' $configfile
