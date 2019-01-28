# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    carName = scrapy.Field()    #总的车名称
    carId = scrapy.Field()
    engine = scrapy.Field()  # 发动机
    gearbox = scrapy.Field()  # 变速箱
    lwh = scrapy.Field()  # 长*宽*高(mm)
    bodywork = scrapy.Field()  # 车身结构
    maxSpeed = scrapy.Field()  # 最高车速(km/h)
    sits = scrapy.Field()  # 座位数(个)    
    fuelForm = scrapy.Field()  # 燃料形式
    gearboxName = scrapy.Field()  # 简称
    gearboxblocks = scrapy.Field()  # 挡位个数
    gearboxType = scrapy.Field()  # 变速箱类型
    