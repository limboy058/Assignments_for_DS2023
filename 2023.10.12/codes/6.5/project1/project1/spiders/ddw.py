import scrapy
from project1.items import Project1Item

class DdwSpider(scrapy.Spider):
    name = "ddw"
    allowed_domains = ["search.dangdang.com","product.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.00.00.00.00-as8589934592%3A8589934622.html"]

    def parse(self, response):
        for lli in response.xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li"):
            item=Project1Item()
            next_url=lli.xpath("p[1]/a/@href")[0].extract()
            next_url="http:"+next_url
            # print(next_url)
            item['url']=next_url
            # http://product.dangdang.com/29611001.html
            print("载入二层url")
            yield scrapy.Request(url=next_url,callback=self.getnext,meta={'item':item})

    def getnext(self,response):
        print("进入第二层爬取数据...")
        item=response.meta['item']
        item['writer']="".join(response.xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/span[1]//text()").extract()).replace(" ","")
        item['name']=response.xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/h1/text()")[0].extract().strip().replace(" ","")
        item['price']="".join(response.xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[6]/div[2]/div[1]/div[1]/p[2]//text()").extract()).strip().replace(" ","")
        item['info']=response.xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/h2/span[1]/text()")[0].extract().strip().replace(" ","")
        item['date']=response.xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/span[3]/text()")[0].extract().replace(u'\xa0', '').replace(" ","")
        item['house']=response.xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/span[2]/a/text()")[0].extract().replace(" ","")
        return item
