# -*- coding: utf-8 -*-
import os
import uuid

# import config

import aria2_utils

        
def find_index(arr,item):
    for dd in arr:
        if dd==item:
            return 1
    return -1
    
# def getUrlCompletePath(url):
#     r = data_source.pause_file_name(url)
#     #print r['filename'],r['type'], r['source'], r['yeardays'], r['date']
#     return os.path.join(cmpdir, r['type'], r['source'], r['yeardays'][0:4], r['yeardays'][4:7], r['filename'])


#加载配置文件
# CFG = config.load('datacenter_download.conf')

# dir = CFG['path_for_orders']
# dldir = CFG["path_for_download"]
# cmpdir = CFG["path_for_complete"]


#准备连接aria2下载服务器
aria2 = aria2_utils.Aria2('127.0.0.1',6800)


#先寻找已经完成任务
tasks=aria2.getCompleteTasks()
# #将完成的任务转移到合适的目录
# for gid in tasks:
#     url=tasks[gid]
#     print gid
#     print url
#
#
#     r = data_source.pause_file_name(url)
#     src = os.path.join(dldir, r['filename'])
#     dst = getUrlCompletePath(url)
#
#     dst_dir= os.path.dirname(dst)
#     print "%s --> %s" % (src, dst)
#
#
#     if os.path.isdir(dst_dir)==False:
#         os.makedirs(dst_dir)
#     if os.path.isfile(dst)==True:
#         dst=dst+"."+str(uuid.uuid1())
#     try:
#         os.rename(src,dst)
#     except:
#         pass
#     src_aria2=src+".aria2"
#     if os.path.isfile(src_aria2):
#         os.remove(src_aria2)
#     aria2.removeTask(gid)
#
# #将历史完成任务转移到合适的目录
# files = os.listdir(dldir)
# for filename in files:
#     r = data_source.pause_file_name(filename)
#     #检查文件是否可以判断出类型
#     if r.has_key('type')==False:
#         continue
#     src = os.path.join(dldir, r['filename'])
#
#     #检查文件是否为.aria2
#     if src[-6:]==".aria2":
#         #print "A",src
#         continue
#
#     #检查文件是否有对应的.aria2文件
#     if os.path.isfile(src+'.aria2'):
#         #print "B",src
#         continue
#
#     dst = getUrlCompletePath(filename)
#     print src,"===>",dst
#
#     dst_dir= os.path.dirname(dst)
#
#     if os.path.isdir(dst_dir)==False:
#         os.makedirs(dst_dir)
#     if os.path.isfile(dst)==True:
#         dst=dst+"."+str(uuid.uuid1())
#     try:
#         os.rename(src,dst)
#     except:
#         pass
    
    
    
#重启失败的任务
aria2.restartErrorTasks()

urls=[]
files = os.listdir(dir)
#读取所有任务的URL
for file in files:
    path = os.path.join(dir, file)
    for line in open(path):
        url=line.strip('\n')
        urls.append(unicode(url))
    os.remove(path)
    
urls = list(set(urls))        

#读取已在aria2系统中的URL
exist_urls =  aria2.getUrls()


#检查URL是否已经下载完成或者存在aria2中
ndl_urls=[]

for url in urls:
    r = find_index(exist_urls, url)
    if r>=0:
        continue
    # path = getUrlCompletePath(url)
    # if os.path.isfile(path):
    #     continue
    ndl_urls.append(url)

#增添任务到aria2中    
print "add url:%d" % len(ndl_urls)
print aria2.addTasks(ndl_urls)    