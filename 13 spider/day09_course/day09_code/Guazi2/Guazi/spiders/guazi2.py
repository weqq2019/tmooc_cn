# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    allowed_domains = ['www.guazi.com']
    # 1、删掉start_urls
    # 2、重写start_requests()方法
    def start_requests(self):
        """把所有要抓取的URL地址交给调度器入队列"""
        for o in range(1,6):
            url = 'https://www.guazi.com/dachang/buy/o{}/#bread'.format(o)
            # 交给调度器入队列
            yield scrapy.Request(url=url, callback=self.parse_one_page, cookies=self.get_cookies())

    def get_cookies(self):
        """处理字符串的cookie为字典"""
        cook_str = 'uuid=cefa207a-d907-4904-a7bf-0d640d2d1601; ganji_uuid=8660622401359177404740; lg=1; antipas=71999O67V68xXH13626I68798f555; clueSourceCode=%2A%2300; sessionid=35757a4f-647a-45fa-8dec-adaf99472a24; close_finance_popup=2020-04-30; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22cefa207a-d907-4904-a7bf-0d640d2d1601%22%2C%22ca_city%22%3A%22langfang%22%2C%22sessionid%22%3A%2235757a4f-647a-45fa-8dec-adaf99472a24%22%7D; gps_type=1; user_city_id=1001737; cityDomain=dachang; lng_lat=116.897746_39.826467; preTime=%7B%22last%22%3A1588234631%2C%22this%22%3A1588066415%2C%22pre%22%3A1588066415%7D'
        cookies = {}
        for kv in cook_str.split('; '):
            key = kv.split('=')[0]
            value = kv.split('=')[1]
            cookies[key] = value

        return cookies

    def parse_one_page(self, response):
        """解析提取数据：名称、链接、价格"""
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            # 给 items.py 中的类GuaziItem实例化
            item = GuaziItem()
            item['name'] = li.xpath('./a[1]/@title').get()
            item['link'] = 'https://www.guazi.com' + li.xpath('./a[1]/@href').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()

            # 把详情页链接交给调度器入队列
            # meta参数：在不同的解析函数之间传递数据
            yield scrapy.Request(url=item['link'], meta={'item':item}, callback=self.parse_two_page)

    def parse_two_page(self, response):
        """二级页面解析函数：提取公里数、排量、类型"""
        # meta: 先到的调度器 - 又到了下载器 - 又作为了response的属性 传递给了指定callback解析函数
        item = response.meta['item']
        item['km'] = response.xpath('//ul[@class="assort clearfix"]/li[2]/span/text()').get()
        item['displace'] = response.xpath('//ul[@class="assort clearfix"]/li[3]/span/text()').get()
        item['typ'] = response.xpath('//ul[@class="assort clearfix"]/li[4]/span/text()').get()

        yield item





