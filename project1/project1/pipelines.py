# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class Project1Pipeline:
    def process_item(self, item, spider):
        print(item)
        return item

class save_to_csv_Pipeline(object):
    def __init__(self):
        self.file = open('books.csv', 'w', encoding='utf-8',newline='')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['书名', '价格', '信息', '日期','出版社'])
    def process_item(self, item, spider):
        self.csvwriter.writerow([item["name"], item["price"], item["info"], item["date"],item["house"]])
        return item
    def close_spider(self, spider):
        self.file.close()