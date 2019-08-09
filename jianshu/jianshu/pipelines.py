# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json

class JianshuPipeline(object):

    def open_spider(self, spider):
        self.file = open('content4.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 每一条信息保存在一行 '\n'
        self.file.write(content)

        return item

    def close_spider(self, spider):
        self.file.close()

