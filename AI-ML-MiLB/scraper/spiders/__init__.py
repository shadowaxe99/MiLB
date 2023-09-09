# AI-ML-MiLB/scraper/spiders/__init__.py

import scrapy

class MlbSpider(scrapy.Spider):
    name = 'mlb'
    start_urls = ['https://www.mlb.com/']

    def parse(self, response):
        # Parse the MLB website and extract relevant data
        # ...


class MilbSpider(scrapy.Spider):
    name = 'milb'
    start_urls = ['https://www.milb.com/']

    def parse(self, response):
        # Parse the MiLB website and extract relevant data
        # ...