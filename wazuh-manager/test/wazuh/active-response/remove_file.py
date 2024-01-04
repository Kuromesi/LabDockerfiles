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
    path = val['parameters']['alert']['syscheck']['path']
    os.system("rm %s"%path)