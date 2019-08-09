# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from jianshu.items import JianshuItem
import re

class HomePageSpider(scrapy.Spider):
    name = 'home_page'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']
    #/users/recommended?seen_ids=&count=15&only_unfollowed=true'
    def __init__(self):
        self.headers ={
            'authority': 'www.jianshu.com',
            'scheme': 'https',

            #加上会报错，DEBUG: Crawled (406)
            #'accept': 'application/json',
            #或者改成
            'accept': 'application/json, text/javascript, */*; q=0.01',

            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '__guid=163745081.721398177172433000.1542009676606.2869; __yadk_uid=bdvylAVwtcwNsOtNCXav3mIiImhHzTvG; read_mode=day; default_font=font2; locale=zh-CN; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1564650577,1564802316,1565078474,1565146419; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1565146419; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216706f068362b9-07316266714d9c-3c604504-1049088-16706f06837218%22%2C%22%24device_id%22%3A%2216706f068362b9-07316266714d9c-3c604504-1049088-16706f06837218%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Fwww.so.com%2Flink%3Fm%3DaurAMaYad69npzX1zgGJa2NieF6sjX%252B4%252FnAj6AzJDDkpeXsu16Pe%252Fh7WKdJK%252FtxGh0UcxgPHBt2Zz8K6d%22%2C%22%24latest_referrer_host%22%3A%22www.so.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22%22%7D; monitor_count=4',

            'referer': 'https://www.jianshu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',

        }
    def start_requests(self):
        yield Request('https://www.jianshu.com/',headers=self.headers)

    def parse(self, response):

        for content in response.xpath("//div[@class = 'content']"):
            print('*'*100)
            item = JianshuItem()

            title = content.xpath("a/text()").extract()  #标题
            dirll = re.search("\d+\.\d+", content.xpath("div/span[1]/text()")[1].get()).group(0)  #钻
            author = content.xpath("div/a/text()").get()  #作者
            comment = re.search("\d+", content.xpath("div/a[2]/text()")[1].get()).group(0)  #评论
            fabulous = content.xpath("div/span[2]/text()").get()   #点赞数

            item['title'] = title
            item['dirll'] = dirll
            item['author'] = author
            item['comment'] = comment
            item['fabulous'] = fabulous

            yield item




