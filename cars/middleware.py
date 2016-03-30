#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: 刘红波
@license: ***
@contact: super_sponge@163.com
@see: https://github.com/super-sponge

@version: 0.0.1
@todo[0.0.2]: a new module

@note: a comment
@attention: please attention
@bug: a exist bug
@warning: warnings
'''

from scrapy.exporters import CsvItemExporter
from scrapy.utils.project import get_project_settings

class OrderCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        settings = get_project_settings()
        delimiter = settings.get('CSV_DELIMITER', ',')

        kwargs['delimiter'] = delimiter
        #
        # fileds = os.environ.get('SCRAPY_SPIDER_NAME', 'DEFAULT')
        # fields_to_export = settings.get('FIELDS_TO_EXPORT_' + fileds, [])
        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export :
            kwargs['fields_to_export'] = fields_to_export

        super(OrderCsvItemExporter, self).__init__(*args, **kwargs)

if __name__ == '__main__':
    pass