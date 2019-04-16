# -*- coding: utf-8 -*-
import scrapy
import re
import  pandas as pd


class BingerSpider(scrapy.Spider):
    name = 'binger'
    allowed_domains = ['bing.com']
    start_urls = []
    data = pd.read_csv('/home/deepak/Desktop/bingScraper/input.csv')
    data = data['keywords']

    count = pd.read_csv('/home/deepak/Desktop/bingScraper/count.csv')
    count = count['states']
    for d in data:
        for e in count:
            start_urls.append('https://www.bing.com/search?q=site:linkedin.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:linkedin.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:linkedin.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:linkedin.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')

            start_urls.append('https://www.bing.com/search?q=site:instagram.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:instagram.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:instagram.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:instagram.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')

            start_urls.append('https://www.bing.com/search?q=site:facebook.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:facebook.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:facebook.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:facebook.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')

            start_urls.append('https://www.bing.com/search?q=site:twitter.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:twitter.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:twitter.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:twitter.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')
            
            start_urls.append('https://www.bing.com/search?q=site:Viadeo.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:Viadeo.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:Viadeo.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:Viadeo.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')

            start_urls.append('https://www.bing.com/search?q=site:pinterest.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:pinterest.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:pinterest.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:pinterest.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')



            start_urls.append('https://www.bing.com/search?q=site:myspace.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:myspace.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:myspace.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:myspace.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')


            start_urls.append('https://www.bing.com/search?q=site:plus.google.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:plus.google.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:plus.google.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:plus.google.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')



            start_urls.append('https://www.bing.com/search?q=site:skyrock.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:skyrock.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:skyrock.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:skyrock.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')

        

            start_urls.append('https://www.bing.com/search?q=site:Badoo.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:Badoo.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:Badoo.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:Badoo.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')



            start_urls.append('https://www.bing.com/search?q=site:trombi.com "gmail.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:trombi.com "yahoo.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:trombi.com "msn.com" '+'"'+d+'"'+'"'+e+'"')
            start_urls.append('https://www.bing.com/search?q=site:trombi.com "ymail.com" '+'"'+d+'"'+'"'+e+'"')



    def parse(self, response):
        x = response.xpath('//body//text()').extract()
        text = ''.join(x)
        email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text)
        
        for x in email:
            yield{
                'email':x
            }
            


        # follow pagination link
        next_page_url = response.xpath('//*[@title="Next page"]/@href').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)



