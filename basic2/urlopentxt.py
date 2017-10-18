# -*- encoding: utf-8 -*- #
__author__ = 'fzh'
from urllib import *

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
txtStr = str(textPage.read())
print txtStr