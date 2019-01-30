# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Tencent.settings import *
import pymongo
import pymysql

class TencentPipeline(object):
    def process_item(self, item, spider):
        print("===============")
        print(item["zhname"])
        print(item["zhtype"])
        print(item["zhnum"])
        print(item["zhaddress"])
        print(item["zhtime"])
        print(item["zhlink"])
        print("===============")
        return item

class MongoPipeline(object):
    def  __init__(self):
        # 连接对象
        self.conn = pymongo.MongoClient(host = MONGODB_HOST, port = MONGODB_PORT)
        # 库对象
        self.db = self.conn[MONGODB_DB]
        # 集合对象
        self.myset = self.db[MONGODB_SET]
    def process_item(self, item, spider):
        # 把一个item转为字典数据类型, 利用dict方法
        d = dict(item)
        self.myset.insert_one(d)
        # 千万别忘返回 item
        return item

class MysqlPipeline(object):
    def __init__(self):
        # 数据库连接对象
        self.db = pymysql.connect(host = MYSQL_HOST,
                                  user = MYSQL_USER,
                                  password = MYSQL_PWD,
                                  database = MYSQL_DB,
                                  charset = "utf8")
        # 游标对象
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        ins = "insert into jobs values(%s,%s,%s,%s,%s,%s)"
        l = [item["zhname"].strip(),
             item["zhtype"].strip(),
             int(item["zhnum"].strip()),
             item["zhaddress"].strip(),
             item["zhtime"].strip(),
             item["zhlink"].strip()
             ]
        print("开始写入")
        self.cursor.execute(ins, l)
        print("提交")
        self.db.commit()
        print("提交完毕")
        return item
    # process_item处理完成后会执行此方法
    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
        print("mysql数据库断开连接")