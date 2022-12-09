# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SystemicLupusErythematosusItem(scrapy.Item):
    TargetID = scrapy.Field()
    TargetName = scrapy.Field()
    TargetType = scrapy.Field()
    Disease = scrapy.Field()
    Drugs = scrapy.Field()
