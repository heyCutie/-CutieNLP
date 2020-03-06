# -*- coding: utf-8 -*-
from urllib import parse

import scrapy

from my_spider.items import MySpiderItem


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['stackoverflow.blog']
    start_urls = ['https://stackoverflow.com/search?q=google']

    def start_requests(self):
        urls = []
        _url = 'https://stackoverflow.com/search?page={}&tab=Relevance&q=google'

        for i in range(34):
            urls.append(_url.format(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 提取帖子的所有url地址
        url_list = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), "question-summary ")]')
        print(len(url_list))

        for url in url_list:
            item = MySpiderItem()
            print(url.attrib['id'])
            item['_id'] = url.attrib['id']
            item['questions'] = url.xpath('div[2]/div[1]/h3/a/text()').extract()
            print(item['questions'])
            item['votes'] = url.xpath('div[1]/div/div[1]/div/span/strong/text()').extract()
            item['answers'] = url.xpath('div[1]/div/div[2]/strong/text()').extract()
            item['links'] = url.xpath('div[2]/div[1]/h3/a/@href').extract()
            yield item


    # def parse_detail(self, response):
    #
    #     title = response.css('.core_title_txt::text').extract()
    #
    #     authors = response.css('.p_author_name.j_user_card::text').extract()
    #
    #     content_list = response.css('.d_post_content.j_d_post_content::text').extract()