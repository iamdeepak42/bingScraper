# -*- coding: utf-8 -*-
import scrapy
import re



class BingerSpider(scrapy.Spider):
    name = 'binger'
    allowed_domains = ['bing.com']
    start_urls = ["https://www.bing.com/search?q=site%3Ainstagram.com+%22gmail.com%22+%22Paris%22"]

    def parse(self, response):

        for i in range(1,11):
            x =response.xpath('//*[@class="b_algo"][{}]//text()'.format(i)).extract()
            y =''.join(x)
            email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",y)
            
            yield{
                'email': email
            }
            


        # follow pagination link
        next_page_url = response.xpath('//*[@title="Next page"]/@href').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)



