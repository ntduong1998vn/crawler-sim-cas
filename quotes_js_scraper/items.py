# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class Article(scrapy.Item):
    url = scrapy.Field()
    short_desc = scrapy.Field()
    title = scrapy.Field()
    published_at = scrapy.Field()
    content = scrapy.Field()
