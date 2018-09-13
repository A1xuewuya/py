# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobboleArticleItem(scrapy.Item):
    title = scrapy.Field()
    cover_img = scrapy.Field()
    public_time = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
    star_num = scrapy.Field()
    bookmark_num = scrapy.Field()
    comment_num = scrapy.Field()