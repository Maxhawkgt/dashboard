#!/bin/bash
# This program gets the public IP address using /PATH_TO_SCRIPT/myip.sh and pushes
# the result to the rc_custom Influxdb database located on 192.168.0.9

ext_ip=$(/PATH_TO_SCRIPT/myip.sh)

curldata="ipaddr,agent_host=xarr,host=monitor address=\"$ext_ip\""

curl -i -XPOST "http://192.168.0.9:8086/write?db=rc_custom&precision=s" --data-binary "$curldata"
