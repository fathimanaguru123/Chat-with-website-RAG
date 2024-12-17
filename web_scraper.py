import scrapy

class UniversitySpider(scrapy.Spider):
    name = 'university_spider'
    start_urls = ['https://www.stanford.edu/']

    def parse(self, response):
        yield {'text': response.css('p::text').getall()}
