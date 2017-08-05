# -*- encoding: utf-8 -*- #
__author__ = 'fzh'

import requests
from bs4 import BeautifulSoup
"""
 Request session demo
"""
def request_kaola():
    with requests.Session() as s:
        header = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
                   "Cookie":'davisit=1; __da_ntes_utmfc=utmcsr%3Dwww.kaola.com%7Cutmccn%3D(prom)%7Cutmcmd%3Dprom%7Cutmpclid%3D__da_FJWpB0_JGMwy9; __nteskl_xk=1478347218160; KAOLA_NEW_USER_COOKIE=no; _jzqy=1.1480166561.1480166561.1.jzqsr=baidu.-; NTES_KAOLA_NEW_CUST=0; usertrack=3/zPBVhiHnW1o1vPAwnjAg==; __kaola_usertrack=20161227155555711396; _da_ntes_uid=20161227155555711396; _ntes_nnid=9ac2a2b0d35944daa14cdb38956e99a2,1482825358660; _jzqx=1.1482825359.1482825359.1.jzqsr=kaola%2Ecom|jzqct=/.-; NETEASE_WDA_UID="feizhang365@163.com#|#1434347479900"; P_INFO=feizhang365@163.com|1482825385|1|kaola|11&22|US&1482717732&urs#hub&420100#10#0#0|135350&0|kaola_check|feizhang365@163.com; _ntes_nuid=a743c9a76ef7e66efb7f447d97f3e43f; _adwr=55934509%230; NTES_KAOLA_RV=1398983_1483185893265_0|1423061_1483185856697_0|4758_1480166590510_0|1357554_1479691722200_0|13806_1478349802431_0|1366976_1478347218180_0|1262366_1465193133069_0|28447_1463710420073_0|33762_1462947783442_0|20664_1460609608775_0|29155_1451874540477_0|20661_1451874453206_0|4617_1451266024697_0|15526_1444381454699_0|6354_1444360756868_0|14918_1442475866087_0|9725_1442286308217_0|5487_1441422605663_0|5488_1441422410029_0|8477_1441422375546_0; SHIPPING_TO_CITY_CODE_NEW=420100; JSESSIONID-WKL-8IO=l%5CPbLjd9oUVZvLJoyxByipONnqaf4PfxEEzqE8M%2BVfVEuGuoyZCvLWS6rJEVNvmQukwEcHzJ2jSDoT0m1VPv%5CdK%2B8p2%5CNRdLPwbs4GI5jp6f0ph4KI8iIDMi9gEBt%5CluUqml%2BWaH6khiz7H8f2srwUMXAZGwPadGKwvl30SW1qh5bZlE%3A1483427553368; _klhtxd_=31; KAOLA_PERSISTENT_SESSION_COUNT=2; NTES_SESS=sRrTG.JBjQKXeEBGF0xZsAH2KdngiAhn_IlLUNOJ0fruIBoZIK0.mFiCFxxBi.D.0lkSjURsAKCuJ3rkFOs_EgBJfo4yqf5j9PYB.S7.nWZ41aHahN_RjtoSr48z5tjxn2aeioYkqx_O66annqNqxVLNaCRo.ePYHJlc5bfVzkLgExxITSuhjkdt.; NTES_PASSPORT=yBnpCOPkQKnXz2_OjYYlf88.zjVxV9RBlwtlcK7gepG13iTX3xgZlsydskkiyZ_ZgnJz6RTAOOcZjqen3D2QchCeerqddVBC7JNd3iakELHJ9; _jzqckmp=1; _adwp=55934509.6611110214.1478347117.1483185803.1483341154.7; _adwc=55934509; __ag_cm_=gtdb; __utma=243297311.515972009.1478347117.1483185802.1483341153.7; __utmc=243297311; __utmz=243297311.1482825359.5.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __da_ntes_utma=2525167.1906984639.1478347127.1483185803.1483341154.7; __da_ntes_utmz=2525167.1478347127.2.10.utmcsr%3Dwww.kaola.com%7Cutmccn%3D(prom)%7Cutmcmd%3Dprom%7Cutmpclid%3D__da_FJWpB0_JGMwy9; Hm_lvt_645b0165bab4840cd77ab93b4bc41821=1482825361,1483185803; Hm_lpvt_645b0165bab4840cd77ab93b4bc41821=1483341601; _ga=GA1.2.515972009.1478347117; ag_fid=TQhEP7ipBL4EKd1F; __xsptplus421=421.6.1483341155.1483341602.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23%2314zmVVdMkrV8kY2G8Nf1WGY2by7o4t8H%23; _jzqa=1.3764444820651901400.1478347118.1483185803.1483341154.7; _jzqc=1; MKAOLA=6ae2bfb6ca75c5be12d8fd0d880637c41c899915; kl_newpopup=1; _pzfxuvpc=1478347117408%7C6289802229756489114%7C33%7C1483341832357%7C7%7C6790604749122778646%7C9971974112847100629; davisit=2; __da_ntes_utma=2525167.1906984639.1478347127.1483185803.1483341154.7; __da_ntes_utmz=2525167.1478347127.2.10.utmcsr%3Dwww.kaola.com%7Cutmccn%3D(prom)%7Cutmcmd%3Dprom%7Cutmpclid%3D__da_FJWpB0_JGMwy9; __utma=163396704.515972009.1478347117.1483341610.1483341610.1; __utmc=163396704; __utmz=163396704.1483341610.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); NTESwapSI=40CEF3F634FB320881E25363100DB821.hzayq-haitao-wap12.server.163.org-8010'}
        r = s.get("http://m.kaola.com/",headers = header)
        # print(r.text)
        soup = BeautifulSoup(r.text,'html.parser')
        # print(soup)
        # print(r.request.headers)
        imgs = soup.find_all("img")
        print(imgs);


def request_dydata():
    with requests.session() as s:
        header = {
            'Accept':'application/json, text/plain, */*',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Pragma':'no-cache',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
            'Cookie':'JSESSIONID=DB570D398463A468E199BF24935646A2; gr_user_id=2b7d2322-6ef5-4daf-8715-5b7b5c2f517a; Hm_lvt_ea3d567ad66d89d77e372bdac5622926=1477648705,1477819974,1477923613,1478670485; uid=w-0zz8VD7spRqOLc33wWT5xzc52K6a0zEXKGmGUh74x4cruHsbLO-Zc-XX7iE3GjnmND--E01E9AGmFD9dSaE7vq-lfzhMLUdW1MJq-bZoCEk6-zYWf6ygZyaE_OMs6bqWB_mgMLlQaANXVBO2NkqQd0IJYGNdJ-hA6E0GO4Gf_76w..; login=%7B%22loginName%22%3A%22figo%22%2C%22nickName%22%3A%22%E9%98%BF%E9%A3%9E%22%2C%22ico%22%3A%22http%3A%2F%2Fimage.dydata.io%2F97161y59lolr41vE95.png%22%7D; Hm_lvt_07397da1b7bf662b93ece50bb615febf=1481180768,1481765077,1482284602,1482975921; Hm_lpvt_07397da1b7bf662b93ece50bb615febf=1483407199; dataSearch=%7B%7D; chartType=%5B%7B%22description%22%3A%22%E9%A5%BC%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cpie_chart.svg%22%2C%22id%22%3A1%2C%22name%22%3A%22chart-pie%22%7D%2C%7B%22description%22%3A%22%E7%BA%BF%E5%BD%A2%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cline_graph.svg%22%2C%22id%22%3A3%2C%22name%22%3A%22chart-line%22%7D%2C%7B%22description%22%3A%22%E6%9F%B1%E7%8A%B6%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cbar_graph.svg%22%2C%22id%22%3A4%2C%22name%22%3A%22chart-bar%22%7D%2C%7B%22description%22%3A%22%E6%95%A3%E7%82%B9%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cscatterplot.svg%22%2C%22id%22%3A6%2C%22name%22%3A%22chart-scatter%22%7D%2C%7B%22description%22%3A%22%E9%9B%B7%E8%BE%BE%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cradar_chart.svg%22%2C%22id%22%3A7%2C%22name%22%3A%22chart-radar%22%7D%2C%7B%22description%22%3A%22%E5%85%B3%E7%B3%BB%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cnetwork_diagram.svg%22%2C%22id%22%3A10%2C%22name%22%3A%22chart-force%22%7D%2C%7B%22description%22%3A%22%E6%A0%91%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Ctreemap.svg%22%2C%22id%22%3A11%2C%22name%22%3A%22chart-tree%22%7D%2C%7B%22description%22%3A%22%E6%A1%91%E5%9F%BA%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Csandkey.svg%22%2C%22id%22%3A12%2C%22name%22%3A%22chart-sandkey%22%7D%2C%7B%22description%22%3A%22%E7%AE%B1%E7%BA%BF%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cbox_plot.svg%22%2C%22id%22%3A14%2C%22name%22%3A%22chart-boxplot%22%7D%2C%7B%22description%22%3A%22%E5%9C%B0%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cpoint%20map.svg%22%2C%22id%22%3A15%2C%22name%22%3A%22chart-map%22%7D%2C%7B%22description%22%3A%22%E6%BC%8F%E6%96%97%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Cfunnel.svg%22%2C%22id%22%3A16%2C%22name%22%3A%22chart-funnel%22%7D%2C%7B%22description%22%3A%22%E6%97%A5%E5%8E%86%E5%9B%BE%22%2C%22icon%22%3A%22svg-icons%5C%5Cchart%5C%5Ccalendar.svg%22%2C%22id%22%3A17%2C%22name%22%3A%22chart-pie%22%7D%5D; chartSearch=%7B%22chartStyle%22%3A%22tpl%22%2C%22order%22%3A%22date%22%2C%22page%22%3A1%7D',
        }
        r = s.get("http://dydata.io/article",headers = header)
        print(r.text)
        # soup = BeautifulSoup(r.text, 'html.parser')
        # articles = soup.select("")


if __name__ == "__main__":
    # request_kaola()
    request_dydata()