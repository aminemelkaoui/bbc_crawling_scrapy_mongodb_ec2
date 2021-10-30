# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BbccralingItem(scrapy.Item):
    # define the fields for your item here like:
    timing = scrapy.Field()
    headline_text_full = scrapy.Field()
    image = scrapy.Field()
    headline_report = scrapy.Field()
    