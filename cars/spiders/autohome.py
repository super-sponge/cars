# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
import json
import sys, re

reload(sys)
sys.setdefaultencoding('gbk')

from cars.items import CarsItem


class AutohomeSpider(CrawlSpider):
    name = 'autohome'
    allowed_domains = ['autohome.com.cn']
    # start_urls = ['http://www.autohome.com.cn/3627','http://www.autohome.com.cn']
    start_urls = ['http://www.autohome.com.cn/3627']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.autohome.com.cn/[\d]+/#pvareaid=[\d]+$'), callback='parse_page',
             follow=True),
        # Rule(LinkExtractor(allow=r'http://www.autohome.com.cn/[\d]+/#pvareaid=[\d]+$'), callback='parse_page', follow=True),
    )

    # 需要抽取的数据
    dataHeader = {'name': u'车型名称',
                  'prices': u'厂商指导价(元)',
                  'factory': u'厂商',
                  'level': u'级别',
                  'engine': u'发动机',
                  'gearbox': u'变速箱',
                  'lwh': u'长*宽*高(mm)',
                  'bodywork': u'车身结构',
                  'maxSpeed': u'最高车速(km/h)',
                  'acceleration100': u'官方0-100km/h加速(s)',
                  'trueAcceleration100': u'实测0-100km/h加速(s)',
                  'brake': u'实测100-0km/h制动(m)',
                  'fuelConsumption': u'实测油耗(L/100km)',
                  'MFuelConsumption': u'工信部综合油耗(L/100km)',
                  'groundClearance': u'实测离地间隙(mm)',
                  'vehicleWarranty': u'整车质保',
                  # 下面是车身信息
                  'length': u'长度(mm)',
                  'wide': u'宽度(mm)',
                  'high': u'高度(mm)',
                  'wheelbase': u'轴距(mm)',
                  'frontGauge': u'前轮距(mm)',
                  'backGauge': u'后轮距(mm)',
                  'MinimumGroundClearance': u'最小离地间隙(mm)',
                  'kerbMass': u'整备质量(kg)',
                  'bodywork': u'车身结构',
                  'doors': u'车门数(个)',
                  'sits': u'座位数(个)',
                  'fuelCapacity': u'油箱容积(L)',
                  'LuggageCapacity': u'行李厢容积(L)',
                  # 下面是发动机器信息
                  'engineType': u'发动机型号',
                  'displacement': u'排量(mL)',
                  'airIntakeForm': u'进气形式',
                  'cylinderArrangement': u'气缸排列形式',
                  'cylinders': u'气缸数(个)',
                  'valvesPerCylinder': u'每缸气门数(个)',
                  'compressionRatio': u'压缩比',
                  'valveActuatingMechanism': u'配气机构',
                  'bore': u'缸径(mm)',
                  'stroke': u'行程(mm)',
                  'maximumHorsepower': u'最大马力(Ps)',
                  'maximumPower': u'最大功率(kW)',
                  'maximumPowerSpeed': u'最大功率转速(rpm)',
                  'maxTorque': u'最大扭矩(N·m)',
                  'maximumTorqueSpeed': u'最大扭矩转速(rpm)',
                  'engineSpecifictechnology': u'发动机特有技术',
                  'fuelForm': u'燃料形式',
                  'fuelLabel': u'燃油标号',
                  'oilSupplyMode': u'供油方式',
                  'cylinderHeadMaterial': u'缸盖材料',
                  'cylinderMaterial': u'缸体材料',
                  'EnvironmentalStandards': u'环保标准',
                  # 变速箱
                  'gearboxName': u'简称',
                  'gearboxblocks': u'挡位个数',
                  'gearboxType': u'变速箱类型',
                  # 地盘
                  'drivingMode': u'驱动方式',
                  'frontSuspensionType': u'前悬架类型',
                  'rearSuspensionType': u'后悬架类型',
                  'AssistType': u'助力类型',
                  'bodyStructure': u'车体结构',
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
        optionIndexStart = response.body.find(optionKey)
        optionIndexEnd = -1
        if optionIndexStart != -1:
            optionIndexEnd = response.body.find(';', optionIndexStart)
        if optionIndexEnd != -1:
            optionStr = response.body[optionIndexStart + len(optionKey):optionIndexEnd]
            optionStr = optionStr.decode('gb18030').encode('utf-8')
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
                    for k, v in self.dataHeader.iteritems():
                        self.extractValue(v, k, basicInfo, cars)

            carName = response.xpath('//div[@class="subnav-title-name"]/a/text()').extract()
            for k, v in cars.iteritems():
                il = ItemLoader(item=CarsItem(), response=response)
                il.add_value('carName', carName)
                il.add_value('carId', k)
                for sk, sv in v.iteritems():
                    il.add_value(sk, sv)
                yield il.load_item()

    def extractValue(self, nameZH, nameEn, baseInfo, car):
        if baseInfo['name'] == nameZH:
            for carInfo in baseInfo['valueitems']:
                v1 = car.get(carInfo['specid'], dict())
                if len(v1) == 0:
                    car[carInfo['specid']] = v1
                v1[nameEn] = carInfo['value']
