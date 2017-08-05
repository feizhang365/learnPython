# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

import requests

def download_image():
    r = requests.get("https://avatars1.githubusercontent.com/u/1308874?v=3&s=40");
    print(r.status_code)
    with open("feilogo.png",'wb') as fd:
        for chunk in r.iter_content(128):
            fd.write(chunk)
    r.close()

if __name__ == '__main__':
    download_image()
