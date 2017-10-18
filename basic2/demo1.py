# -*- coding:utf-8 -*-
__author__ = 'fzh'
from urllib import *
from bs4 import BeautifulSoup
# 爬取 http://www.allitebooks.com/ 所有pdf 下载地址
# 进入页面取得页面中进入详情页面地址
pagehtml = urlopen("http://www.allitebooks.com/")
bsObj = BeautifulSoup(pagehtml.read(),"html5lib")
# print(bsObj)
linkList = bsObj.select('div.entry-body > header > h2 > a')
#进入详情页面抓取下载pdf文件地址
for links in linkList:
    detailurl = links.get('href')
    detailhtml = urlopen(detailurl)
    detailObj = BeautifulSoup(detailhtml.read(),"html5lib")
    pdflink = detailObj.select("span.download-links > a")
    # print pdflink
    pdf_download_url = pdflink[0].get('href')
    print pdf_download_url
