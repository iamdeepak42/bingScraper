# -*- coding: utf-8 -*-
import scrapy
import re
import  pandas as pd


class BingerSpider(scrapy.Spider):
    name = 'binger'
    allowed_domains = ['bing.com']
    # start_urls = ["]
    data = pd.read_csv('input.csv')
    data = data['keywords']
    for d in data:

        start_urls.append('https://www.bing.com/search?q=site:linkedin.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:linkedin.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:linkedin.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:linkedin.com "ymail.com" '+'"'+d+'"')

        start_urls.append('https://www.bing.com/search?q=site:instagram.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:instagram.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:instagram.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:instagram.com "ymail.com" '+'"'+d+'"')

        start_urls.append('https://www.bing.com/search?q=site:facebook.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:facebook.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:facebook.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:facebook.com "ymail.com" '+'"'+d+'"')

        start_urls.append('https://www.bing.com/search?q=site:twitter.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:twitter.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:twitter.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:twitter.com "ymail.com" '+'"'+d+'"')
        
        start_urls.append('https://www.bing.com/search?q=site:Viadeo.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:Viadeo.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:Viadeo.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:Viadeo.com "ymail.com" '+'"'+d+'"')

        start_urls.append('https://www.bing.com/search?q=site:pinterest.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:pinterest.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:pinterest.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:pinterest.com "ymail.com" '+'"'+d+'"')



        start_urls.append('https://www.bing.com/search?q=site:myspace.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:myspace.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:myspace.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:myspace.com "ymail.com" '+'"'+d+'"')


        start_urls.append('https://www.bing.com/search?q=site:plus.google.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:plus.google.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:plus.google.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:plus.google.com "ymail.com" '+'"'+d+'"')



        start_urls.append('https://www.bing.com/search?q=site:skyrock.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:skyrock.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:skyrock.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:skyrock.com "ymail.com" '+'"'+d+'"')


        start_urls.append('https://www.bing.com/search?q=site:Badoo.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:Badoo.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:Badoo.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:Badoo.com "ymail.com" '+'"'+d+'"')



        start_urls.append('https://www.bing.com/search?q=site:trombi.com "gmail.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:trombi.com "yahoo.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:trombi.com "msn.com" '+'"'+d+'"')
        start_urls.append('https://www.bing.com/search?q=site:trombi.com "ymail.com" '+'"'+d+'"')



    def parse(self, response):
    
        for i in range(1,11):
            x =response.xpath('//body//text()'.format(i)).extract()
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



