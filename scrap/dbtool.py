# -*- coding: utf-8 -*-

import pymysql

db_connection = None
db_cursor = None

def ConnectDB():
    global db_connection, db_cursor
    dbconfig =dict(host='localhost', port=3306, user='root', passwd='root', db='pydb')
    try:
        db_connection = pymysql.connect(**dbconfig)
        db_cursor = db_connection.cursor()
    except :
        print "Connect DB Error!"
        exit()
        
        
def ExecuteSQL(_sql):
    global db_connection, db_cursor
    try:
        db_cursor.execute(_sql)
    except:
        print "Exceute [ \n%s\n         ] Error!" % _sql
        exit()
        
    return db_cursor

if __name__ == '__main__':
    ConnectDB()
    print db_connection
    # bookurl = 'http://file.allitebooks.com/20160513/ReactJS%20by%20Example%20-%20Building%20Modern%20Web%20Applications%20with%20React.pdf'
    # cur = ExecuteSQL("select * from allitebook where pdfurl = '%s'" %bookurl)
    cur = ExecuteSQL("select * from allitebook")
    for row in cur:
        print(row)
