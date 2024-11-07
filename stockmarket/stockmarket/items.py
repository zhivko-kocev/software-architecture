# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    code = scrapy.Field()
    date = scrapy.Field()
    last_transaction = scrapy.Field()
    max_transaction = scrapy.Field()
    min_transaction = scrapy.Field()
    avg_transaction = scrapy.Field()
    cash_flow_per = scrapy.Field()
    quantity = scrapy.Field()
    cash_flow = scrapy.Field()