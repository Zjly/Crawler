import re
import scrapy

from Crawler.items.TTDItem import TTDItem


class TTDSpider(scrapy.Spider):
    name = "TTD"
    allowed_domains = ["https://db.idrblab.net"]
    start_urls = []

    urls = "https://db.idrblab.net/ttd/search/ttd/target?search_api_fulltext=rheumatoid%20arthritis&page="

    # 结束页码
    end_page = 17

    for i in range(end_page + 1):
        start_urls.append(urls + str(i))

    def parse(self, response):
        p = re.compile(r'[(](.*?)[)]', re.S)
        target_info = response.xpath('//*[@class="ttd-table table table-bordered ttd-result-item"]')
        for target in target_info:
            item = TTDItem()
            # 获取TargetID
            item["TargetID"] = target.xpath('tbody/tr[1]/th[1]/text()').extract_first()

            # 获取TargetName
            TargetName = target.xpath('tbody/tr[1]/td/text()').extract_first()
            item["TargetName"] = re.findall(p, TargetName)[0]

            # 获取TargetType
            item["TargetType"] = target.xpath('tbody/tr[2]/td/text()').extract_first()

            # 获取Disease
            item["Disease"] = target.xpath('tbody/tr[3]/td/text()').extract_first()

            # 获取Drugs
            item["Drugs"] = target.xpath('tbody/tr[4]/td[1]/text()').extract_first().replace('\n', '').replace(' ', '')

            yield item
