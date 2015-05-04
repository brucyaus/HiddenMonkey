# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["youtube.com"]
    start_urls = (
        'http://www.youtube.com/',
    )

    def parse(self, response):
        pass
