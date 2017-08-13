# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.doban.com']
    start_urls = ['http://movie.doban.com/']

    def start_requests(self):
        file_object = open('movie_name.txt', 'r')

        try:
            url_head = "https://movie.douban.com/subject_search?search_text="
            for line in file_object:
                self.start_urls.append(url_head + line + "&cat=1002")
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            file_object.close()

    def parse(self, response):
        pass














