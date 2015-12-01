# -*- coding: utf-8 -*-


import urllib2, urllib, os, time
import cookielib
import json
import time
import random

#print "%d" % (time.time()*1000)

#print urllib.quote_plus("BVHeQCLhSsA/Nysn+8P8mRKENH8b/H2zHf3YPEq/3MY=")
#exit()

#管理redirect
class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        print "302------------->"
        print req
        print fp
        print code
        print msg
        print headers
        print "-----------------"
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)


class MyHTTPErrorProcessor(urllib2.HTTPErrorProcessor):

    def http_response(self, request, response):
    
        code, msg, hdrs = response.code, response.msg, response.info()

        # only add this line to stop 302 redirection.
        if code == 302: 
            #print "-------------------"
            s = hdrs['Location']
            #print s
            #print "-------------------"
            if s.find("http://bjdl.gscloud.cn/")>=0:
                return response
                
            return urllib2.HTTPErrorProcessor.http_response(self, request, response)

        if not (200 <= code < 300):
            response = self.parent.error(
                'http', request, response, code, msg, hdrs)
        return response

    https_response = http_response        
        

#使用session管理
cj = cookielib.MozillaCookieJar()
cookies = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookies,  MyHTTPErrorProcessor)
#opener = urllib2.build_opener(cookies)

def print_result(r):
    print
    print r['url']
    print "==============================================================================="
    print r['code'], r['msg']
    print r['info']
    print "-------------------------------------------------------------------------------"
    #print r['response'][:200],".\n.\n.\n.\n.\n.",r['response'][-200:]
    print r['response'].decode('utf-8')
    print "-------------------------------------------------------------------------------"
    #time.sleep(1)

def url_http(url,formdata=None):
    if formdata==None:
        f = opener.open(url)
    else:
        data_encoded = urllib.urlencode(formdata)
        f = opener.open(url, data_encoded)
        
    r = {}
    r['response'] = f.read()
    r['code'] = f.code
    r['url'] = f.url
    r['msg'] = f.msg
    r['info'] = f.info()
    return r
    
    
url_main = "http://www.gscloud.cn/"    
url_login_html = "http://www.gscloud.cn/login.shtml?from=http%3A%2F%2Fwww.gscloud.cn%2F"    
url_login_post = "http://www.gscloud.cn/loginCsdb.shtml"
url_user_top = "http://www.gscloud.cn/user_top.shtml?v=%d"
url_csearch_json = "http://search.gscloud.cn/search/csearch_json.shtml?callback=jsonp_callback&areaName=&areaNameEncoded=&east=0&edate=&north=0&productId=421&qType=0&sdate=&south=0&stCode=&stName=&tableName=dem_metadata_gdemv2&west=0&wkt=&tableInfo=%7B%22offset%22%3A0%2C%22pageSize%22%3A10%2C%22totalPage%22%3A1%2C%22totalSize%22%3A0%2C%22sortSet%22%3A%5B%5D%2C%22filterSet%22%3A%5B%5D%7D"
url_csearch_json = url_csearch_json.replace("10", "11000")
url_list_data= "http://www.gscloud.cn/listdata/listdata_new.shtml?from=&&productId=421"
url_download = "http://www.gscloud.cn/download.do?id=%s&tableName=dem_metadata_gdemv2&type=data&userid=%s&site=dgdl"


#打开首页
r = url_http(url_main)
print_result(r)


#打开登录页
r = url_http(url_login_html)
print_result(r)

#登录
login_data={}
login_data['from']="http%3A%2F%2Fwww.gscloud.cn%2F"
login_data['username']="youlan224@163.com"
login_data['password']="yanshan"
r = url_http(url_login_post,login_data)
print_result(r)

#打开user信息
r = url_http(url_user_top % (time.time()*1000))
print_result(r)

''' 将所有的文件信息list出来
#search信息
r = url_http(url_csearch_json) 
#print_result(r)
s=r['response']
m=s.find("{")
n=s.rfind("}")
ss = s[m:n+1]


data = json.loads(ss)
print data['productId']
print data['tableName']
print data['total']
print len(data['data'])

f=open("url_csearch_json.json","w")
f.write( json.dumps(data, indent=4) )
f.close()
'''

#打开list页面
r = url_http(url_list_data) 
s=r['response']
m = s.find("userid: \"")
ss = s[m:m+80]
m=ss.find("\"")
n=ss.rfind("\"")
ss = ss[m:n+1]
print ss
userid = urllib.quote_plus(ss[1:-1])
print userid

id = '8129'
id = '505'
#下载数据
'''
r = url_http(url_download % ( id, userid) )
f=open( id+".zip","wb")
content = r['response']
f.write( content )
f.close()
print id, len(content)
print "----------------------------------------------"
print r['msg']
print "----------------------------------------------"
print r['info']
'''

def get_download_url(id, userid):
    url = url_download % ( id, userid)
    try:
        f = opener.open(url, timeout=10)
    except:
        pass
    #print "download "
    '''
    data_list=[]
    data=f.read(100)
    data_list.append(data)
    print "get 100"
    '''
    #print f.info()
    return f.info()['Location']
    
    
def save_data( data ):
    #return
    print "#",
    f=open("url_csearch_json.json","w")
    f.write( json.dumps(data, indent=4) )
    f.close()
    
data = json.loads(open("url_csearch_json.json").read())
print data['productId']
print data['tableName']
print data['total']
print len(data['data'])

i=1
for item in data['data']:
    if item.has_key('url'):
        continue
    while True:
        try:
            url = get_download_url(item['id'], userid)
            print ".",
        except:
            print "!",
            continue
        item['url'] = url
        break
    
    i+=1
    if i%64==0:
        save_data(data)
        
save_data(data)
