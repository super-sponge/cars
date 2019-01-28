爬取汽车之家数据
================

## scrapy 安装
yum -y install epel-release
yum -y install python-pip
yum -y install python-devel
yum -y install gcc
pip install scrapy

## scrapy 代码下载及运行
yum install -y git

git clone https://github.com/super-sponge/cars.git
	
###
字段
carName,carId,engine,gearbox,lwh,bodywork,maxSpeed,sits,fuelForm,gearboxName,gearboxblocks,gearboxType

create database cars default character set utf8;
grant all on cars.* TO 'cars'@'%' IDENTIFIED BY 'cars123';

CREATE TABLE IF NOT EXISTS cars (
   carName VARCHAR(64),
   carId int,
   engine VARCHAR(64),
   gearbox VARCHAR(64),
   lwh VARCHAR(32),
   bodywork VARCHAR(8),
   maxSpeed int,
   sits int,
   fuelForm VARCHAR(8),
   gearboxName VARCHAR(24),
   gearboxblocks int,
   gearboxType VARCHAR(24)
)DEFAULT CHARSET=utf8;