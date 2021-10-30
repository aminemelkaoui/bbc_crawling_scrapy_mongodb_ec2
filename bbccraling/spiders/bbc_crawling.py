import scrapy
from bbccraling.items import BbccralingItem


class BbcCrawlingSpider(scrapy.Spider):
    name = 'bbc_crawling'
    allowed_domains = ['bbc.com']
    start_urls = ['http://bbc.com/news']

    def parse(self, response):
         
        linkurl = response.css(
            'a.gs-c-promo-heading.gs-o-faux-block-link__overlay-link.gel-pica-bold.nw-o-link-split__anchor::attr(href)')

        for lien in linkurl:
            yield response.follow(lien.get(), callback=self.parse_stories)

    def parse_stories(self, response):
        # Specify the main tag name from which we will extract the links to crawl
        headlines = response.css(
            'article.ssrcss-1mc1y2-ArticleWrapper.e1nh2i2l6')
        item = BbccralingItem()
        # extracting the main information from the crawled link 
        for hdln in headlines:

            item['timing'] = hdln.css('time::attr(datetime)').get(),
            item['headline_text_full'] = hdln.css(
                'h1.ssrcss-gcq6xq-StyledHeading.e1fj1fc10::text').get().strip(),
            item['image'] = hdln.css('img::attr(src)').get()
            item['headline_report'] = hdln.css(
                'p.ssrcss-1q0x1qg-Paragraph.eq5iqo00::text').getall()
            yield item
            # if you want to get a local batch json file of the crawled data  
            # yield{
            #     'timing':hdln.css('time::attr(datetime)').get(),
            #     'headline_text_full': hdln.css('h1.ssrcss-gcq6xq-StyledHeading.e1fj1fc10::text').get().strip(),
            #     'image':hdln.css('img::attr(src)').get(),
            #     'headline_report':[hdln.css('p.ssrcss-1q0x1qg-Paragraph.eq5iqo00::text').get().strip()],
            # }
