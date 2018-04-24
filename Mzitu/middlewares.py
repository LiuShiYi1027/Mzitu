# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

class MeiZiTu(object):
    def process_request(self, request, spider):
        '''设置headers和切换请求头
        :param request: 请求体
        :param spider: spider对象
        :return: None
        '''
        referer = request.meta.get('referer', None)
        if referer:
            request.headers['referer'] = referer
