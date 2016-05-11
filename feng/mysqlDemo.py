# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

import mysql.connector
mysql_cfg = dict(user='root', password='root', database='feidb', use_unicode=True)
#conn = mysql.connector.connect(user='root', password='root', database='feidb', use_unicode=True)
conn = mysql.connector.connect(**mysql_cfg)
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print values
cursor.close()
conn.close()
