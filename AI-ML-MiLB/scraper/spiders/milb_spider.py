import scrapy

class MilbSpider(scrapy.Spider):
    name = 'milb_spider'
    start_urls = ['http://www.example.com']

    def parse(self, response):
        # Parse the response and extract the required data
        # ...

        yield {
            'data': extracted_data
        }