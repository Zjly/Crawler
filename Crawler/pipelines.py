# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import xlsxwriter as xw


class CrawlerPipeline:
    def __init__(self):
        # 初始化excel
        self.workbook = xw.Workbook("TTD.xlsx")
        self.worksheet1 = self.workbook.add_worksheet("sheet1")
        self.worksheet1.activate()
        self.insert_data = ['TargetID', 'TargetName', 'TargetType', 'Disease', 'Drugs']
        self.row_index = 1

    def process_item(self, item, spider):
        # 写入当前item
        for i in range(5):
            row = 'A' + str(self.row_index)
            self.worksheet1.write_row(row, [self.insert_data[i], item[self.insert_data[i]]])
            self.row_index += 1

        row = 'A' + str(self.row_index)
        self.worksheet1.write_row(row, [])
        self.row_index += 1

        return item

    def close_spider(self, spider):
        self.workbook.close()
