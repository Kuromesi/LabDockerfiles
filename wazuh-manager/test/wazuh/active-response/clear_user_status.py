#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import MySQLdb
import sys
import json

def clear_status():
    with open('/var/ossec/etc/database.json', 'r') as f:
        database = json.load(f)
    db = MySQLdb.connect(database['mysql']['server'], database['mysql']['username'], database['mysql']['password'], database['mysql']['database'], database['mysql']['port'])
    cursor = db.cursor()
    sql = "DELETE FROM user_status WHERE 1"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print (e)
        print ("Error: unable to delete data")
    db.close()

if __name__ == "__main__":
    clear_status()
