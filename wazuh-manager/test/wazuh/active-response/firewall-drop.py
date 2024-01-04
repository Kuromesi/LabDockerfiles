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
    src_ip = val['parameters']['alert']['data']['src_ip']
    process = os.popen("iptables -C INPUT -p all -s %s -j DROP; echo $?"%src_ip)
    output = process.readlines()[0]
    output = output.strip()
    process.close()
    if (output != "0"):
        os.system("iptables -A INPUT -p all -s %s -j DROP"%src_ip)
        
    process = os.popen("iptables -C FORWARD -p all -s %s -j DROP; echo $?"%src_ip)
    output = process.readlines()[0]
    output = output.strip()
    process.close()
    if (output != "0"):
        os.system("iptables -I FORWARD -p all -s %s -j DROP"%src_ip)