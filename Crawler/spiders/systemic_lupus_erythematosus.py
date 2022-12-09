import json
import re
import scrapy

from Crawler.items.SystemicLupusErythematosusItem import SystemicLupusErythematosusItem


class SystemicLupusErythematosusSpider(scrapy.Spider):
    name = "systemic_lupus_erythematosus"


    links = ["https://db.idrblab.net/ttd/search/ttd/target?search_api_fulltext=systemic%20lupus%20erythematosus&page=0"]
    start_urls = links

    def parse(self, response):
        for news in response.xpath('//<table class="ttd-table table table-bordered ttd-result-item>'):
            item = SystemicLupusErythematosusItem()
            # 获取文章标题
            item["title"] = news.xpath('.//h1/text()').extract_first()
            # 获取文章时间
            item["time"] = news.xpath('.//div[@class="info-source"]/span[2]/text()').extract_first()
            # 获取文章内容并清除其中的标签
            content = news.xpath('.//div[@class="info-content"]').extract_first()
            content = re.compile(r'<[^>]+>', re.S).sub('', content)
            item["content"] = content
            yield item
