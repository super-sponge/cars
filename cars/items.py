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

    name = scrapy.Field()  # 车型名称,
    prices = scrapy.Field()  # 厂商指导价(元)
    factory = scrapy.Field()  # 厂商
    level = scrapy.Field()  # 级别
    engine = scrapy.Field()  # 发动机
    gearbox = scrapy.Field()  # 变速箱
    lwh = scrapy.Field()  # 长*宽*高(mm)
    bodywork = scrapy.Field()  # 车身结构
    maxSpeed = scrapy.Field()  # 最高车速(km/h)
    acceleration100 = scrapy.Field()  # 官方0-100km/h加速(s)
    trueAcceleration100 = scrapy.Field()  # 实测0-100km/h加速(s)
    brake = scrapy.Field()  # 实测100-0km/h制动(m)
    fuelConsumption = scrapy.Field()  # 实测油耗(L/100km)
    MFuelConsumption = scrapy.Field()  # 工信部综合油耗(L/100km)
    groundClearance = scrapy.Field()  # 实测离地间隙(mm)
    vehicleWarranty = scrapy.Field()  # 整车质保
    # 下面是车身信息	= scrapy.Field()
    length = scrapy.Field()  # 长度(mm)
    wide = scrapy.Field()  # 宽度(mm)
    high = scrapy.Field()  # 高度(mm)
    wheelbase = scrapy.Field()  # 轴距(mm)
    frontGauge = scrapy.Field()  # 前轮距(mm)
    backGauge = scrapy.Field()  # 后轮距(mm)
    MinimumGroundClearance = scrapy.Field()  # 最小离地间隙(mm)
    kerbMass = scrapy.Field()  # 整备质量(kg)
    bodywork = scrapy.Field()  # 车身结构
    doors = scrapy.Field()  # 车门数(个)
    sits = scrapy.Field()  # 座位数(个)
    fuelCapacity = scrapy.Field()  # 油箱容积(L)
    LuggageCapacity = scrapy.Field()  # 行李厢容积(L)
    # 下面是发动机器信息	= scrapy.Field()
    engineType = scrapy.Field()  # 发动机型号
    displacement = scrapy.Field()  # 排量(mL)
    airIntakeForm = scrapy.Field()  # 进气形式
    cylinderArrangement = scrapy.Field()  # 气缸排列形式
    cylinders = scrapy.Field()  # 气缸数(个)
    valvesPerCylinder = scrapy.Field()  # 每缸气门数(个)
    compressionRatio = scrapy.Field()  # 压缩比
    valveActuatingMechanism = scrapy.Field()  # 配气机构
    bore = scrapy.Field()  # 缸径(mm)
    stroke = scrapy.Field()  # 行程(mm)
    maximumHorsepower = scrapy.Field()  # 最大马力(Ps)
    maximumPower = scrapy.Field()  # 最大功率(kW)
    maximumPowerSpeed = scrapy.Field()  # 最大功率转速(rpm)
    maxTorque = scrapy.Field()  # 最大扭矩(N·m)
    maximumTorqueSpeed = scrapy.Field()  # 最大扭矩转速(rpm)
    engineSpecifictechnology = scrapy.Field()  # 发动机特有技术
    fuelForm = scrapy.Field()  # 燃料形式
    fuelLabel = scrapy.Field()  # 燃油标号
    oilSupplyMode = scrapy.Field()  # 供油方式
    cylinderHeadMaterial = scrapy.Field()  # 缸盖材料
    cylinderMaterial = scrapy.Field()  # 缸体材料
    EnvironmentalStandards = scrapy.Field()  # 环保标准
    # 变速箱	= scrapy.Field()
    gearboxName = scrapy.Field()  # 简称
    gearboxblocks = scrapy.Field()  # 挡位个数
    gearboxType = scrapy.Field()  # 变速箱类型
    # 地盘	= scrapy.Field()
    drivingMode = scrapy.Field()  # 驱动方式
    frontSuspensionType = scrapy.Field()  # 前悬架类型
    rearSuspensionType = scrapy.Field()  # 后悬架类型
    AssistType = scrapy.Field()  # 助力类型
    bodyStructure = scrapy.Field()  # 车体结构
