# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request, FormRequest


class CommentSpider(scrapy.Spider):
    name = 'comment'
    start_urls = ["https://i.gamersky.com/user/login"]



    def __init__(self):

        #定义请求头
        self.header = {
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                        'X-Requested-With':'XMLHttpRequest',
                    }


    def parse(self, response):
        data = {
            'username': '226003720@qq.com',  #账号
            'loginpassword': 'gz142404',   #密码
            'persistent': 'true',   #这俩i货固定就行
            'showCode': 'false',

        }
        url = "https://i.gamersky.com/user/login"
        #callback=self.comment 去执行comment
        return  scrapy.FormRequest(url, formdata= data ,headers=self.header, dont_filter=False, callback=self.comment)


    def comment(self,response):
        print('*'*10)
        print(response.text)
        # {'StatusCode': 1, 'Message': 'ok', 'OtherParameter': 'no'}
        # 如果账号密码错误，将看见
        # {'StatusCode': -5, 'Message': '用户名、邮箱、电话号码不存在！', 'OtherParameter': 'no'}
        #将返回的respons转成字典
        res = json.loads(response.text)

        if res['Message'] != 'ok':
            print(res['Message'])
        else:
            com = {
                'jsondata': '{"sid":"1206174","content":"1谁",}'
            }
            return  scrapy.FormRequest('http://cm.gamersky.com/api/addcommnet', formdata=com, headers=self.header, callback = self.com_success)
    def com_success(self,response):
        succ = json.loads(response.text)
        print(succ)
        #{'status': 'ok', 'body':
        if succ['status'] == 'ok':
            print('评论成功')





