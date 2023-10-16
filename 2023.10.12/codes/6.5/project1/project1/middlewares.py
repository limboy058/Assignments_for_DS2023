# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class Project1SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class Project1DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        request.cookies={
            '__permanent_id':'20230305124806201199631247429654017',
            'ddscreen':'2',
            '__visit_id':'20231016145328376364904807711675890', 
            '__out_refer':'',
            'dest_area':'country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0',
            'secret_key':'f71ab10a622030d2305c3dc7fb1e1c13',
            'login_dang_code':'20231016150018258135795881d7dbec',
            'sessionID':'pc_eb017fd6e1cddb8065c228616353e428d5e7a1976e99d2d9778fb8f3b357fbab',
            'USERNUM':'92OEjMxZcndS+5DrAU/b0Q==',
            'login.dangdang.com':'.ASPXAUTH=/TzpQBubRl0GSaMF0aquJlbC+soLVjpad15DchPa471AJY1/+sMfIQ==', 
            'dangdang.com':'email=MTkzNzA1NzA3MzA4MDA2OUBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=&display_id=1599300250595&customerid=Rp0F6PoEtxwm0jQ2nag1kA==&viptype=MRU0GDn88nQ=&show_name=193****0730',
            'LOGIN_TIME':'1697439837238',
            '__rpm':'%7Cs_605253.451680112839%2C451680112840.1.1697440317813',
            '__trace_id':'20231016151158876343687936500897116'
        }
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
