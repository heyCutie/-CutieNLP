# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    questions = scrapy.Field()
    votes = scrapy.Field()
    answers = scrapy.Field()
    links = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into stackoverflow(id, questions, votes, answers, links)
            values (%s,%s,%s,%s,%s)
        """
        params = (self["_id"], self["questions"], self["votes"], self["answers"], self["links"])

        return insert_sql, params

