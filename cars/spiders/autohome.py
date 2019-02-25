# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
import json
import sys, re

#reload(sys)
#sys.setdefaultencoding('gbk')

from cars.items import CarsItem


class AutohomeSpider(CrawlSpider):
    name = 'autohome'
    allowed_domains = ['autohome.com.cn']
    # start_urls = ['http://www.autohome.com.cn/3627','http://www.autohome.com.cn']
    start_urls = ['http://www.autohome.com.cn/3627','http://www.autohome.com.cn/4817']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.autohome.com.cn/[\d]+/#pvareaid=[\d]+$'), callback='parse_page',
             follow=True),
        # Rule(LinkExtractor(allow=r'http://www.autohome.com.cn/[\d]+/#pvareaid=[\d]+$'), callback='parse_page', follow=True),
    )

    # 需要抽取的数据
    dataHeader = {'engine': u'发动机',
                  'gearbox': u'变速箱',
                  'lwh': u'长*宽*高(mm)',
                  'bodywork': u'车身结构',
                  'maxSpeed': u'最高车速(km/h)',
                  'sits': u'座位数(个)',
                  'fuelForm': u'燃料形式',
                  'gearboxName': u'简称',
                  'gearboxblocks': u'挡位个数',
                  'gearboxType': u'变速箱类型'
                  }

    def start_requests(self):

        for url in self.start_urls:
            m =re.match(r'http://www.autohome.com.cn/([\d]+)', url)
            if m:
                carId = m.group(1)
                configUrl = 'http://car.autohome.com.cn/config/series/%s.html' % carId
                yield scrapy.Request(configUrl, self.parse_config, meta={'carId': carId})
            yield self.make_requests_from_url(url)



    def parse_page(self, response):
        carId = response.url.split('/')[-2]
        configUrl = 'http://car.autohome.com.cn/config/series/%s.html' % carId
        yield scrapy.Request(configUrl, self.parse_config, meta={'carId': carId})

    def parse_config(self, response):
        carId = response.meta['carId']
        self.logger.info('A response from %s and Id is %s' % (response.url, carId))
        optionKey = 'var config = '
        optionIndexStart = response.body.decode('utf-8').find(optionKey)
        optionIndexEnd = -1
        if optionIndexStart != -1:
            optionIndexEnd = response.body.decode('utf-8').find(';', optionIndexStart)
        if optionIndexEnd != -1:
            optionStr = response.body.decode('utf-8')[optionIndexStart + len(optionKey):optionIndexEnd]
            optionJson = json.loads(optionStr)
            cars = dict()

            for topItem in optionJson['result']['paramtypeitems']:
                # if topItem['name'] == u'基本参数':
                #     for basicInfo in topItem['paramitems']:
                #         for k, v in self.dataHeader.iteritems():
                #             self.extractValue(v, k, basicInfo, cars)
                # if topItem['name'] == u'车身':
                #     for basicInfo in topItem['paramitems']:
                #         for k, v in self.dataHeader.iteritems():
                #             self.extractValue(v, k, basicInfo, cars)
                for basicInfo in topItem['paramitems']:
                    for k, v in self.dataHeader.items():
                        self.extractValue(v, k, basicInfo, cars)

            carName = response.xpath('//div[@class="subnav-title-name"]/a/text()').extract()
            for k, v in cars.items():
                il = ItemLoader(item=CarsItem(), response=response)
                il.add_value('carName', carName)
                il.add_value('carId', str(k).strip('[').strip(']'))
                for sk, sv in v.items():
                    il.add_value(sk, sv)
                yield il.load_item()

    def extractValue(self, nameZH, nameEn, baseInfo, car):
        if baseInfo['name'] == nameZH:
            for carInfo in baseInfo['valueitems']:
                v1 = car.get(carInfo['specid'], dict())
                if len(v1) == 0:
                    car[carInfo['specid']] = v1
                v1[nameEn] = carInfo['value']
