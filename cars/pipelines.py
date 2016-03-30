# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CarsPipeline(object):
    def process_item(self, item, spider):

        #价格去掉单位
        prices = item['prices']
        prices[0] = prices[0].replace(u'万','')
        item['prices'] = prices

        return item
