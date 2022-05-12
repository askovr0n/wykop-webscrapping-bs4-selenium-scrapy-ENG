import scrapy

# Mapping
'''REMEMBER TO CHANGE THE BOOLEAN VALUE BELOW !!!! '''
START_100_SCRAPE = True


def adjust_loop():
    last_loop = 0
    if START_100_SCRAPE:
        last_loop = 120
    else:
        last_loop = 3  # For testing
    return last_loop

class Wykop(scrapy.Item):

    title = scrapy.Field()
    nickname = scrapy.Field()
    likes = scrapy.Field()
    dislikes = scrapy.Field()
    views = scrapy.Field()
    hashtags = scrapy.Field()


class WykopSpider(scrapy.Spider):

    name = "wykop"
    allowed_domains = ['wykop.pl']
    start_urls = ["http://www.wykop.pl/strona/" + str(i) + "/" for i in range(1, adjust_loop()+1)]

    def parse(self, response):
        xpath_url = "//div[@class='grid-main m-reset-margin']//ul[@id='itemsStream'][@class = 'comments-stream ']//div[@class='lcontrast m-reset-margin']/h2/a/@href"
        for href in response.xpath(xpath_url)[:1]:
            url = href.get()
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        variables = Wykop()

        variables["title"] = \
            response.xpath("//div[@class='lcontrast m-reset-float m-reset-margin']/h2/span[@class = 'data-wyr']/text()").extract()[0]
        try:
            variables["nickname"] = response.xpath("//div[@class='usercard']//span/b/text()").extract()
        except:
            variables["nickname"] = ''

        try:
            variables["likes"] = response.xpath("//a[@href='#voters']/b/text()").extract()[0]
        except:
            variables["likes"] = ''

        try:
            variables["dislikes"] = response.xpath("//a[@href='#votersBury']/b/text()").extract()[0]
        except:
            variables["dislikes"] = ''

        try:
            variables["views"] = response.xpath("//a[@class='donttouch']//b/text()").extract()[0]
        except:
            variables["views"] = ''

        try:
            variables["hashtags"] = \
                response.xpath(
                "//div[@class='lcontrast m-reset-float m-reset-margin']/div[@class='fix-tagline']/a[position()>1]/text()").extract()
        except:
            variables["hashtags"] = ''

        yield variables
