#!/usr/bin/python3

import sys, os
import json
import time

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
    if 'audit' not in val['parameters']['alert']['data']:
        uid = val['parameters']['alert']['data']['auid']
    else:
        uid = val['parameters']['alert']['data']['audit']['auid']
    result = os.popen('getent passwd %s'%uid)
    result = result.readline()
    user = result.split(":")[0]
    os.system("sudo -u %s DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/%s/bus notify-send 'ALERT' 'YOUR ACTIONS ARE BEING MONITORED'"%(user, uid))
    os.system("sudo passwd -l %s"%user)
    os.system("sudo iptables -P INPUT DROP")
    os.system("sudo iptables -P OUTPUT DROP")
    os.system("sudo iptables -P FORWARD DROP")
    time.sleep(10)
    os.system("sudo pkill -KILL -u %s"%user)