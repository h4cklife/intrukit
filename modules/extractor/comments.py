import scrapy
import scrapy.selector
import scrapy.crawler
import scrapy.http
import re
from multiprocessing import Process, Queue

class Module:
    """
    Module Class
    """
    __title__ = 'extractor.comments'
    __date__ = '2017-11-13'
    __rank__ = 'normal'
    __description__ = 'This is a scrapy spider that will extract comments from the source code of web pages'

    __author__ = 'Intrukit'

    def __init__(self,
                 URLS=None,
                 DOMAINS=None,
                 FEEDFORMAT='json',
                 FEEDURI='results/data/comments_results.json',
                 LOGFILE='results/data/comments_debug.log',
                 LOGLEVEL='DEBUG'):
        """
        __init__(self,
                 URLS=None,
                 DOMAINS=None,
                 FEEDFORMAT='json',
                 FEEDURI='comments_results.json',
                 LOGFILE='comments_debug.log',
                 LOGLEVEL='DEBUG')
                 
        :param URLS: 
        :param DOMAINS: 
        :param FEEDFORMAT: 
        :param FEEDURI: 
        :param LOGFILE: 
        :param LOGLEVEL: 
        
        Initialize the module class with the desired options and default values
        """
        self.__dict__['URLS'] = {"value": URLS, "required": True, "description": "A CSV of URLS to scrape"}
        self.__dict__['DOMAINS'] = {"value": DOMAINS,
                                    "required": True,
                                    "description": "A CSV of DOMAINS allowed. Sets Boundaries."}
        self.__dict__['FEEDFORMAT'] = {"value": FEEDFORMAT, "required": True,
                                        "description": "Feed format. json, csv, xml"}
        self.__dict__['FEEDURI'] = {"value": FEEDURI, "required": True, "description": "Feed output file"}
        self.__dict__['LOGFILE'] = {"value": LOGFILE, "required": True, "description": "Log output file"}
        self.__dict__['LOGLEVEL'] = {"value": LOGLEVEL, "required": True,
                                      "description": "Log level. CRITICAL, ERROR, WARNING, INFO, DEBUG"}

    def run(self):
        """
        run(self)
        :return: 
        
        Modules run function
        """
        class BasicCrawlerItem(scrapy.Item):
            """
            BasicCrawlerItem(scrapy.Item)
            """
            comments = scrapy.Field()
            location_url = scrapy.Field()

        class BasicCrawlerPipeline(object):
            """
            BasicCrawlerPipeline(object)
            """
            def process_item(self, item, spider):
                return item

        class MySpider(scrapy.Spider):
            """
            MySpider(scrapy.Spider)
            """
            name = "comments"
            allowed_domains = str(self.__dict__['DOMAINS']['value']).split(',')
            start_urls = str(self.__dict__['URLS']['value']).split(',')
            custom_settings = {
                'FEED_FORMAT': str(self.__dict__['FEEDFORMAT']['value']),
                'FEED_URI': str(self.__dict__['FEEDURI']['value']),
                'LOG_FILE': str(self.__dict__['LOGFILE']['value']),
                'LOG_LEVEL': str(self.__dict__['LOGLEVEL']['value'])
            }

            def parse(self, response):
                """
                parse(self, resposne)
                
                :param response: 
                :return: 
                
                Parse the response
                """
                hxs = scrapy.selector.Selector(response)

                # CODE for scraping comments
                comments = hxs.xpath('//comment()').extract()
                for comment in comments:
                    com = BasicCrawlerItem()
                    com["comments"] = comment
                    com["location_url"] = response.url
                    yield com

                visited_links = []
                links = hxs.xpath('//a/@href').extract()
                link_validator = re.compile(
                    "^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")

                for link in links:
                    if link_validator.match(link) and not link in visited_links:
                        visited_links.append(link)
                        yield scrapy.http.Request(link, self.parse)
                    else:
                        full_url = response.urljoin(link)
                        visited_links.append(full_url)
                        yield scrapy.http.Request(full_url, self.parse)

        def crawl():
            """
            crawl()
            
            :return: 
            
            Perform the crawl process with MySpider
            """
            """Using CrawletProcess over CrawlerRunner gave us both json output and logging"""
            process = scrapy.crawler.CrawlerProcess({
                'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
            })
            process.crawl(MySpider)
            process.start(stop_after_crawl=True)  # the script will block here until the process is stop()
            print("Done. Press CTRL + C to continue...")

        if self.DOMAINS['value'] \
                and self.URLS['value'] \
                and self.FEEDFORMAT['value'] \
                and self.FEEDURI['value'] \
                and self.LOGFILE['value'] \
                and self.LOGLEVEL['value']:
            """
            This runs our crawl in a separate process and
            just blocks our prompt until user presses ctrl + c when the scan is done.
            Code had to be done this way to get around various issues
            and complications related to twisted.internet.error.ReactorNotRestartable
            """
            try:
                q = Queue()
                p = Process(target=crawl)
                p.start()

                s = False
                while not s:
                    result = q.get()
                    p.join()
                    if result:
                        print("Scan done.")
                        s = True
                        raise result
            except:
                print("\nDropping back to shell..")
        else:
            print("Please set the required options")
