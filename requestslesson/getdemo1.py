# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

import requests
"""
requests get demos
"""
r = requests.get('https://github.com/timeline.json')
status_code = r.status_code
response_txt = r.text

print "status :::" + str(status_code)
print response_txt
