# -*- coding: utf-8 -*-
import scrapy
from items import ProductItem

    
class mobSpyder(scrapy.Spider):
       name = "mobileSpy"
       allowed_domains = ['slonrekomenduet.com']
       start_urls = ['https://slonrekomenduet.com/model/htc-wildfire-s.html','https://slonrekomenduet.com/model/nokia-asha-200.html','https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb.html','https://slonrekomenduet.com/model/htc-desire-310.html','https://slonrekomenduet.com/model/nokia-5230.html','https://slonrekomenduet.com/model/nokia-500.html','https://slonrekomenduet.com/model/nokia-asha-305.html','https://slonrekomenduet.com/model/nokia-lumia-520.html','https://slonrekomenduet.com/model/nokia-lumia-720.html','https://slonrekomenduet.com/model/nokia-x7.html','https://slonrekomenduet.com/model/nokia-e7.html','https://slonrekomenduet.com/model/nokia-asha-500-dual-sim.html','https://slonrekomenduet.com/model/nokia-asha-311.html','https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380.html','https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos.html','https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262.html','https://slonrekomenduet.com/model/htc-one-v.html','https://slonrekomenduet.com/model/htc-desire-v.html']
       def parse(self, response):
           print("processing:"+response.url)
           comment = response.xpath('/html//div[@class="comment"]')
           for comm in comment:
               item = ProductItem()
               data = ' '.join(comm.xpath('.//div[@class="comment_text"]/text()').extract())
               item['otziv']=data.replace('\r', '')
               stars = comm.xpath('.//div[@class="author"]/div[@class="br-theme-css-stars"]/div[@class="br-widget"]/a[@class="br-active"]')
               if len(stars)<=3:
                  item['target']=0
               else:
                  item['target']=1
               yield item
           NEXT_PAGE_SELECTOR = 'html body div#wrapper div#content div div#user_reviews div#more_reviews a::attr(href)'
           next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
           if next_page:
              yield scrapy.Request(
              response.urljoin(next_page),
              callback=self.parse
              )