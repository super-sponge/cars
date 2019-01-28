#!/bin/bash
#Description: 爬取汽车之家部分数据

#Author:root
#Version:1.0
#CreateTime:2019-01-28 13:50:19


base_dir=$(cd `dirname $0`; pwd)
dt=$(date "+%Y%m%d%H%M%S")


outfile=${base_dir}/data/cars_new_$dt.csv
outload=/tmp/cars_load.csv
scrapy crawl autohome  -o $outload -t csv

cd $base_dir
mysql -ucars -pcars123 -D cars < load.sql

mv $outload $outfile