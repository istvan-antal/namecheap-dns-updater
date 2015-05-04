#!/usr/bin/env python
import subprocess
import json
from httplib import HTTPSConnection
from httplib import HTTPConnection
from base64 import b64encode
from time import time
from datetime import datetime
from os import chdir
from os import path

CONFIG_JSON_PATH = "config.json"
IP_FILE_PATH = "current_ip"

chdir(path.dirname(path.realpath(__file__)))

config_file = open(CONFIG_JSON_PATH)
config = json.load(config_file)
config_file.close()

print datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')

c = HTTPConnection("ip.changeip.com")
c.request("GET", "/")
res = c.getresponse()
data = res.read()

current_ip = data.split("\n")[0]

try:
    ip_file = open(IP_FILE_PATH)
    old_ip = ip_file.read().strip()
    ip_file.close()
except IOError:
    old_ip = ""

if current_ip != old_ip:
    print "Old ip: " + old_ip
    print "New ip: " + current_ip

    c = HTTPSConnection("dynamicdns.park-your-domain.com")
    c.request("GET",
        "https://dynamicdns.park-your-domain.com/update?host=" + config['host'] +
        "&domain=" + config['domain'] +
        "&password=" + config['password'] + "&ip=" +current_ip
    )
    res = c.getresponse()
    data = res.read()
    print "Response: " + data

    f = open(IP_FILE_PATH, "w+")
    f.write(current_ip)
    f.close()
else:
    print "No change"