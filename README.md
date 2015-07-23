# amazon-tracker
Tracking price for specific products on amazon.jp

## Preinstall 
* pip install scrapy

## How to use
1. Go to amazon.jp to find which product you want, and copy the product price page URL. Ex: http://www.amazon.co.jp/gp/offer-listing/B00YGHG8J0/ref=dp_olp_new?ie=UTF8&condition=new
2. Edit price_spider.py:
  * goods_url
  * expect_price
3. Run `scrapy crawl price` in this repo root directory.

## Trivial
* Working with `crontab` is better.
* Integrate twitter or other social network API to notifiy the expected price is reached.
