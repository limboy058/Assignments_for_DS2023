import scrapy
from project1.items import Project1Item

class DdwSpider(scrapy.Spider):
    name = "ddw"
    allowed_domains = ["search.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.00.00.00.00-as8589934592%3A8589934622.html"]

    def parse(self, response):
        items=[]
        for lli in response.xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li"):
            item=Project1Item()
            item['name']=lli.xpath("./p[1]/a/text()").extract()[0]
            item['price']=lli.xpath("./p[3]/span[1]/text()").extract()[0].replace(u'\xa5', '¥')
            try:
                item['info']="".join(lli.xpath("./p[5]/span[1]//text()").extract())
                item["date"]=lli.xpath("./p[5]/span[2]/text()").extract()[0].replace('/','')
                item["house"]=lli.xpath("./p[5]/span[3]//text()").extract()[1]
            except:
                item['info']="".join(lli.xpath("./p[6]/span[1]//text()").extract())
                item["date"]=lli.xpath("./p[6]/span[2]/text()").extract()[0].replace('/','')
                item["house"]=lli.xpath("./p[6]/span[3]//text()").extract()[1]
            items.append(item)
        print("已爬取一页")
        return items

