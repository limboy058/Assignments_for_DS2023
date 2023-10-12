# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Project1Item(scrapy.Item):
    name=scrapy.Field()
    price=scrapy.Field()
    info=scrapy.Field()
    date=scrapy.Field()
    house=scrapy.Field()
    pass
