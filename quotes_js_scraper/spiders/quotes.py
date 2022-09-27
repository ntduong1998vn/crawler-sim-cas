import scrapy
from quotes_js_scraper.items import Article
from scrapy_playwright.page import PageMethod
from urllib.parse import unquote


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        url = "http://www.sim.cas.cn/search/?keyword=%25E5%258D%258A%25E5%25AF%25BC%25E4%25BD%2593&searchword=%E5%8D%8A%E5%AF%BC%E4%BD%93"
        yield scrapy.Request(url, meta=dict(
            playwright=True,
            playwright_include_page=True,
            playwright_page_methods=[
                PageMethod("wait_for_selector", ".search-sort.mb10.clearfix"),
            ],
            errback=self.errback,
        ))

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        for quote in response.css('.nav-result .mb20'):
            quote_item = Article()
            quote_item['url'] = quote.css('.mb5>a::attr(href)').get()
            quote_item['short_desc'] = quote.css('.content>p::text').get()
            yield quote_item

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
