# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # 定义基准url
    url = "https://hr.tencent.com/position.php?start="
    start_urls = [url + str(0)]

    def parse(self, response):
        # ba所有的url地址都给调度器入队列
        for i in range(0, 280, 10):
            url = self.url + str(i)
            # scrapy.Request()
            yield scrapy.Request(url, callback=self.parseHtml)

    def parseHtml(self, response):
        item = TencentItem()
        baselist = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for base in baselist:
            item["zhname"] = base.xpath('./td[1]/a/text()').extract()[0]
            item["zhtype"] = base.xpath('./td[2]/text()').extract()
            if item["zhtype"]:
                item["zhtype"] = item["zhtype"][0]
            else:
                item["zhtype"] = "无"
            item["zhnum"] = base.xpath('./td[3]/text()').extract()[0]
            item["zhaddress"] = base.xpath('./td[4]/text()').extract()[0]
            item["zhtime"] = base.xpath('./td[5]/text()').extract()[0]
            item["zhlink"] = base.xpath('./td[1]/a/@href').extract()[0]
            yield item