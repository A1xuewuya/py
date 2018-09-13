# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from urllib import parse

from ArticleSpider.items import JobboleArticleItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # 解析列表页中的所有文章url交给 scrapy下载并进行解析
        article_url_posts = response.css("span.read-more a::attr(href)").extract()
        for article_url in article_url_posts:
            # 如果取到的url不是完整的url  url = parse.urljoin(response.url, article_url)
            yield Request(url=parse.urljoin(response.url, article_url), callback=self.parse_detail)

        # 提取下一页url并交给scrapy下载
        next_url = response.css(".next.page-numbers::attr(href)").extract_first()
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        # 提取文章具体字段
        # xpath选择器
        # //*[@id="post-114228"]/div[1]/h1
        # res_selector = response.xpath('//*[@id="post-114228"]/div[1]/h1/text()')
        # selector_data = res_selector.extract()
        article_title = response.xpath("//div[@class='entry-header']/h1/text()").extract()[0]
        publish_time = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace(
            "·", "").strip()
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        article_content = response.xaaapath("//div[@class='entry']").extract_first()
        star_num = response.xpath("//div[@class='post-adds']//h10/text()").extract_first()
        bookmark_data = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract_first()
        bookmark_re = re.match(".*?(\d+).*", bookmark_data)
        if bookmark_re:
            bookmark_num = int(bookmark_re.group(1))
        else:
            bookmark_num = 0
        comment_data = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        comment_re = re.match(".*?(\d+).*", comment_data)
        if comment_re:
            comment_num = int(comment_re.group(1))
        else:
            comment_num = 0

        # 添加到数据关系映射当中
        article_item = JobboleArticleItem()


        # css选择器
        # article_title = response.css("div.entry-header h1::text").extract_first()
        # public_time = response.css("p.entry-meta-hide-on-mobile::text").extract_first().strip().replace("·", "").strip()
        # tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        # article_content = response.css("div.entry").extract_first()

