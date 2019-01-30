# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    zhname = scrapy.Field()
    # 职位类别
    zhtype = scrapy.Field()
    # 招聘人数
    zhnum = scrapy.Field()
    # 工作地点
    zhaddress = scrapy.Field()
    # 发布时间
    zhtime = scrapy.Field()
    # 详情链接
    zhlink = scrapy.Field()