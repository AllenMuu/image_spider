import scrapy

from image_spider.items import ImageSpiderItem


class imageSpider(scrapy.Spider):
    name = 'imgSpider'
    start_urls = [
        'http://lab.scrapyd.cn/archives/57.html',
        'http://lab.scrapyd.cn/archives/55.html',
    ]

    def parse(self, response):
        item = ImageSpiderItem()  #实例化item
        imgUrls = response.css(".post-content img::attr(src)").extract() # 获取url链接
        item['imgUrl'] = imgUrls

        imgNames = response.css(".post-title a::text").extract_first()
        item['imgName'] = imgNames
        yield item