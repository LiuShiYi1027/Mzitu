# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 下午9:51
# @Author  : LiuShiYi
# @Site    : 
# @File    : spider.py.py
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Mzitu.items import MzituItem
from scrapy import Request


class Spider(CrawlSpider):
    name = 'mzitu' # 爬虫名称
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/all'] # 爬虫的入口地址
    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',),
                           deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item', follow=True),
    )
    img_urls = []

    def parse_item(self, response):
        """
        处理得到的response
        :param response: 下载返回的response
        :return:
        """
        item = MzituItem()

        try:
            item['url'] = response.url
            item['title'] = response.xpath(".//h2/text()").extract()[0]
            item['num'] = int(response.xpath(".//div[@class='pagenavi']//span/text()").extract()[-2])
        except Exception as e:
            print('错误提示'.center(30, '*'))
            print('url:', response.url)
            print('error:', e)
            print(''.center(50, '*'))

        for i in range(1, item['num'] + 1):
            page_url = response.url + '/' + str(i)
            yield Request(page_url, callback=self.img_url)

        item['image_urls'] = self.img_urls

        yield item

    def img_url(self, response):
        """
        处理图片所在的html
        :param response:
        :return:
        """
        # 提取图片的详细url
        img_urls = response.xpath("descendant::div[@class='main-image']/descendant::img/@src").extract()

        # 将图片真实的url添加到img_urls中
        for img_url in img_urls:
            self.img_urls.append(img_url)