# -*- coding:utf-8 -*-
__author__ = 'fzh'
from urllib import *
from bs4 import BeautifulSoup
import aria2_utils
# 爬取 http://www.allitebooks.com/ 所有pdf 下载地址
# 进入页面取得页面中进入详情页面地址
homePage = urlopen('http://www.allitebooks.com/')
bsObj = BeautifulSoup(homePage.read(),"html5lib")
# 抓取页面总数
pageSpan = bsObj.find('span',attrs={'class':'pages'})
pageSizeInfo = pageSpan.contents[0]
pageSize = pageSizeInfo.split(' ')
pageSizeVal = int(pageSize[2])
print'页面总数 :',pageSizeVal
# print(bsObj)
# 进入每页抓取书籍连接
aria2 = aria2_utils.Aria2('127.0.0.1',6800)
for x in range(1,pageSizeVal,1):
    pageOpen = urlopen('http://www.allitebooks.com/page/'+str(x))
    pageObj = BeautifulSoup(pageOpen,"html5lib")
    linkList = pageObj.select('div.entry-body > header > h2 > a')
    #进入详情页面抓取下载pdf文件地址
    for links in linkList:
        detailUrl = links.get('href')
        detailHtml = urlopen(detailUrl)
        detailObj = BeautifulSoup(detailHtml.read(),"html5lib")
        pdfLink = detailObj.select("span.download-links > a")
        # print pdflink
        pdf_download_url = pdfLink[0].get('href')
        aria2.addTask(pdf_download_url)
        print pdf_download_url
