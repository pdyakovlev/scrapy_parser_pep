import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import SPIDER_NAME, ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):

    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        table_bodies = response.css('tbody')

        for tr in table_bodies.css('tr'):
            link_pep_page = tr.css('td').css('a::attr(href)').get()
            link_pep_page += '/'
            if link_pep_page is not None:
                yield response.follow(link_pep_page, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        st = response.css('dt:contains("Status") + dd')
        abbr = st.css('abbr::text').get()
        data = {
            'number': [int(s) for s in title.split() if s.isdigit()][0],
            'name': title,
            'status': abbr
        }
        yield PepParseItem(data)
