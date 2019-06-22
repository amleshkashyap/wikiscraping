import scrapy
import  scrapy_proj.util.parseFile as parseFile


class WikiSpider(scrapy.Spider):
    name = "wiki_spider"

    def start_requests(self):
        #urls = ['http://quotes.toscrape.com/page/1/']
        urls = ['https://en.wikipedia.org/wiki/Museum_of_Pop_Culture']
        #urls = ['https://webcache.googleusercontent.com/search?q=cache:wJ6cT1V_rCYJ:https://www.zomato.com/seattle/canlis-westlake+&cd=1&hl=en&ct=clnk&gl=in']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        with open('museum_pop_culture_bs4.txt', 'a', encoding="utf-8") as outfile:
            newBody = parseFile.getTextFromWikiPage(response.body)
            outfile.write(str(newBody))
            '''
            resp = response.text.split("\n")
            for line in resp:
                if "<p>" in line:
                    newLine = parseFile.getTextFromWikiString(line)
                    outfile.write(newLine)
                    outfile.write("\n")
            '''


class GoogleCacheSpider(scrapy.Spider):
    name = "gcache_spider"

    def start_requests(self):
        #urls = ['http://quotes.toscrape.com/page/1/']
        urls = ['https://webcache.googleusercontent.com/search?q=cache:wJ6cT1V_rCYJ:https://www.zomato.com/seattle/canlis-westlake+&cd=1&hl=en&ct=clnk&gl=in']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        with open('zomato_canlis.txt', 'wb') as outfile:
            outfile.write(response.body)