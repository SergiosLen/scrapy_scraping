# -*- coding: utf-8 -*-

import scrapy
from efsyn.items import EfsynItem

class EfsynSpider(scrapy.Spider):
    name = 'efsyn'
    allowed_domains= ['efsyn.gr']
    start_urls = [
        "http://www.efsyn.gr/search/node?keys=προσφυγ* AND Ευρώπη&author=All&category=3&date_filter[min][date]=01.01.2016&date_filter[max][date]=31.03.2016&field_comic_author_ref_target_id=All&sort_by=created"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        # 
    ]
    # STT=True

    def parse(self,response):
        print response.url,'===================================='
        # if response.xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/div[2]/p/text()')[0].extract() == u'Δεν βρέθηκαν αποτελέσματα.':
        #     print 'here'
        #     return 
        for sel in response.xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li'):
            title= sel.xpath('div/h3/a/text()').extract()
            link= response.urljoin(sel.xpath('div/h3/a/@href')[0].extract())
            # link= sel.xpath('div/h3/a/@href').extract()

            created = sel.xpath('div/div/div[1]/text()').extract()
            desc= sel.xpath('div/div/div[2]/div/div/a/text()').extract()
            # desc= sel.xpath('text()').extract()
                # f.write(response.bo)
                # print title,link,desc
            item=EfsynItem()
            item['title']=title
            item['link']=link
            item['created']=created
            item['desc']=desc

            yield item
       # '/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[11]'  
       # '/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[13]'
       # '/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[13]'
        # '/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[14]'
        # /html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[14]
       # 'html.js body.html.not-front.not-logged-in.no-sidebars.page-search.page-search-node.layout-version-full.sliding-popup-processed div.page_wrapper div.masonry_grid.col-4-3-2-1 div.panel-pane.pane-page-content div div.clearfix div.news_block div.content-width div.col-4-3-2-1 div.col-2-2-2-1 div.panel-pane.pane-views-panes.pane-search-panel-pane-1.column.col-2-2-2-1 div.pane-content.column_padding div.view.view-search.view-id-search.view-display-id-panel_pane_1.view-dom-id-69c4b22b4a42b5803ca8776b969eb065 ul.pager li.pager-next'
        if response.url.split('&')[-1].split('=')[0]!='page':
            next_page= response.xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[11]/a/@href')[0].extract()
            # STT=False
        elif response.url.split('&')[-1].split('=')[0]=='page' :
            myre=response.url.split('&')[-1].split('=')
            nun=myre[-1]
            monon=response.url[:-len(nun)]
            next_page=monon+str(int(nun)+1)



            # next_page= response.xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[13]/a/@href')

        # next_page=response.css('ul.pager li.pager-next')
        
        print next_page,'*********************************************************'
        print response.url.split('&')[-1].split('=')[0]=='page',response.url
        # print next_page,'========================='
        if next_page:

        # self.parse_dir_contents(response)
        # for href in response.xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/ul/li[11]/a/@href'):
            url = response.urljoin(next_page)
            # print url
            yield scrapy.Request(url, callback=self.parse)


    def parse_dir_contents(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        for sel in response.xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li'):
            title= sel.xpath('div/h3/a/text()').extract()
            # link= response.urljoin(sel.xpath('div/h3/a/@href').extract())
            link= sel.xpath('div/h3/a/@href').extract()

            created = sel.xpath('div/div/div[1]/text()').extract()
            desc= sel.xpath('div/div/div[2]/div/div/a/text()').extract()
            # desc= sel.xpath('text()').extract()
                # f.write(response.bo)
                # print title,link,desc
            item=EfsynItem()
            item['title']=title
            item['link']=link
            item['created']=created
            item['desc']=desc
            yield item


# response.xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li