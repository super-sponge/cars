#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from scrapy import cmdline
import  time

if __name__ == '__main__':
    outfile = './data/cars_new_' + time.strftime('%Y%m%d%H%M%S') + '.csv'
    cmd = 'scrapy crawl autohome  -o ' + outfile + ' -t csv'
    print cmd
    cmdline.execute(cmd.split())
