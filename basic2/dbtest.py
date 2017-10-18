# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='pydb')

cur = conn.cursor()

cur.execute("SELECT * FROM allitebook")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()