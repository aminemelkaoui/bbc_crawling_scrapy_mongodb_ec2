# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# create a collection for mongodb databases and the data base


import pymongo
from pymongo import MongoClient


class BbccralingPipeline(object):
    collection_name = 'bbc_crawler' 

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_bbc_crawler(cls, bbc_crawler):
        return cls(
            mongo_uri=bbc_crawler.settings.get('MONGO_URI'),
            mongo_db=bbc_crawler.settings.get('MONGO_DATABASE', 'items')
        )
#delete old data
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri, ssl=True)
        self.db = self.client[self.mongo_db]
        self.db[self.collection_name].delete_many({})
        self.db['bbc_crawl'].delete_many({})

    def close_spider(self, spider):
        self.client.close()
#add new data to data base schema 
    def process_item(self, item, spider):
        data_coun = self.db[self.collection_name].data_coun(
            {"timing": item['timing'], "headline_text_full": item['headline_text_full'], "image": item['image'], "headline_report": item['headline_report']})
        if (data_coun == 0):
            self.db[self.collection_name].insert_one(dict(item))
        return item
