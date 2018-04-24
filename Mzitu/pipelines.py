# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.item import Item
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import pymongo
import re


def strip(path):
    """
    清洗存储路径中的非法字符
    :return:
    """
    path = re.sub(r'[？\\*|“<>:/]', '', str(path))
    return path


class MzituPipeline(object):

    DB_URI = 'mongodb://localhost:27017'
    DB_NAME = 'mzitu'

    def open_spider(self, spider):
        """
        爬虫打开，建立与mongo的连接
        :param spider:
        :return:
        """
        self.client = pymongo.MongoClient(self.DB_URI)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        """
        爬虫关闭，断开与mongo的连接
        :param spider:
        :return:
        """
        self.client.close()

    def process_item(self, item, spider):
        """
        将数据存入mongoDB
        :param item:
        :param spider:
        :return:
        """
        collection = self.db[spider.name]
        picture = dict(item) if isinstance(item, Item) else item
        collection.insert_one(picture)
        return item


class MzituImagesPipeline(ImagesPipeline):


    def file_path(self, request, response=None, info=None):
        """
        :param request: 每一个图片下载管道请求
        :param response:
        :param info:
        :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
        :return: 每套图的分类目录
        """
        item = request.meta['item']
        folder = item['title']
        folder_strip = strip(folder)
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0}/{1}'.format(folder_strip, image_guid)
        return filename

    def get_media_requests(self, item, info):
        """
        :param item: spider.py中返回的item
        :param info:
        :return:
        """
        for img_url in item['image_urls']:
            referer = item['url']
            yield Request(img_url, meta={'item': item,
                                         'referer': referer})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item