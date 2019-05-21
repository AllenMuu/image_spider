# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class ImageSpiderPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img_url in item['imagUrl']:
            yield Request(img_url)

    def file_path(self, request, response=None, info=None):
        # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
        image_guid = request.url.split('/')[-1]  # 提取url前面名称作为图片名。
        return image_guid