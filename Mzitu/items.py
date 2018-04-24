# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MzituItem(Item):
    """
    mzitu item
    """
    title = Field()  # 组图名称
    num = Field()  # 组图数量
    url = Field()  # 组图入口地址
    image_urls = Field() # 每一张图片的详细url