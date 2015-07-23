# -*- coding: utf-8 -*-
import scrapy
import re

class PriceSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['www.amazon.co.jp']
    goods_url = 'http://www.amazon.co.jp/gp/offer-listing/B00YGHG8J0/ref=dp_olp_new?ie=UTF8&condition=new'
    expect_price = 2000
    start_urls = [
        goods_url
    ]
    def __init__(self):
        pass
    def parse(self, response):
        for el in response.css('span.olpOfferPrice::text'):
            str_price = el.extract().strip()
            price_list = re.split(r'\D', str_price)
            int_price = int(price_list[-2] + price_list[-1])
            
            if int_price < self.expect_price:
                msg = '便宜唷～快來買唷～ ' + self.goods_url
                print msg 


            
