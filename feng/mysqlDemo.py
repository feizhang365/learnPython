# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

import mysql.connector
conn = mysql.connector.connect(user='root', password='root', database='feidb', use_unicode=True)
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print values
cursor.close()
conn.close()
