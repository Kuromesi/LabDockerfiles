#!/usr/bin/python3

import sys, os
import json
import re

def parse_fields(argv):
    recv = sys.stdin.readline()
    with open('/root/recv.txt', 'a') as f:
        f.write(recv)
    data = {}
    try:
        data = json.loads(recv)
    except Exception:
        print ("Json parsing failed")
    return data

if __name__ == "__main__":
    val = parse_fields(sys.argv)
    agent = val['parameters']['alert']['agent']['name']
    # result = os.popen("who | cut -d' ' -f1 | sort | uniq")
    # result = result.readlines()
    user = "user"
    uid = "1000"
    os.system("sudo -u %s DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/%s/bus notify-send 'ALERT' 'MALICIOUS BEHAVIOR DETECTED AT %s'"%(user, uid, agent))