# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

import mysql.connector
mysql_cfg = dict(user='root', password='root', database='pydb', use_unicode=True)
#conn = mysql.connector.connect(user='root', password='root', database='feidb', use_unicode=True)
db_conn = None
db_cursor = None
#建立连接
def creatConn():
    global  db_conn,db_cursor
    try:
        db_conn = mysql.connector.connect(**mysql_cfg)
        print db_conn
        db_cursor = db_conn.cursor()
        # return db_conn,db_cursor
    except:
        print "Connect DB Error!"
        exit()
#查询
def findByPDFUrl(pdfurl):
    global  db_conn,db_cursor
    try:
        # db_cursor.execute('select * from allitebook where pdfurl=%s' % pdfurl)
        res = db_cursor.execute('select * from allitebook')
        # if len(res) == 0:
        #     print res
        #     db_cursor.close()
        # else:
        #     print res
        print res
        return db_cursor
    except mysql.connector.Error as err:
        print(err)
        exit(1)
    finally:
        db_conn.close()

if __name__ == '__main__':
    creatConn()
    print db_conn
    bookurl = 'http://file.allitebooks.com/20160513/ReactJS%20by%20Example%20-%20Building%20Modern%20Web%20Applications%20with%20React.pdf'
    findByPDFUrl(bookurl)

