import scrapy


class EximbankroItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
