# -*- coding: utf-8 -*-
import scrapy


class Myspider1Spider(scrapy.Spider):
    name = "MySpider1"
    allowed_domains = ["datall.cn"]
    start_urls = (
        'http://www.datall.cn/',
    )

    def start_requests(self):
        return [scrapy.FormRequest("http://www.datall.cn/db/j_spring_security_check",formdata={'j_username': 'figo', 'j_password': '1111'},callback=self.logged_in)]

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        print response.body
        pass

    def parse(self, response):
        pass
