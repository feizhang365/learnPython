# -*- coding: utf-8 -*-
import os
import aria2_utils

        
def find_index(arr,item):
    for dd in arr:
        if dd==item:
            return 1
    return -1

#准备连接aria2下载服务器
aria2 = aria2_utils.Aria2('127.0.0.1',6800)

#重启失败的任务
aria2.restartErrorTasks()

#读取已在aria2系统中的URL
exist_urls =  aria2.getUrls()
print exist_urls


#检查URL是否已经下载完成或者存在aria2中
ndl_urls=[]

#增添任务到aria2中    
print "add url:%d" % len(ndl_urls)
print aria2.addTasks(ndl_urls)    