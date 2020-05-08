# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
import scrapy
import os

class PptPipeline(FilesPipeline):
    # 重写get_media_requests()方法
    def get_media_requests(self, item, info):
        """把一堆的下载链接交给了调度器入队列"""
        # 把meta包装到请求对象中 request
        yield scrapy.Request(url=item['ppt_download'], meta={'item':item})

    # 重写file_path方法,保存到对应路径
    def file_path(self, request, response=None, info=None):
        # FILES_SOTRE: /home/tarena/ppt/
        # filename: 工作总结PPT/小清新.zip     item['parent_name']/item['ppt_name'].zip
        # scrapy.Request()中所有的参数,都可以作为请求对象 request 的属性
        item = request.meta['item']
        filename = '{}/{}{}'.format(
            item['parent_name'],
            item['ppt_name'],
            os.path.splitext(request.url)[1]
        )

        return filename







