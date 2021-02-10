import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import ItalycaindosuezItem
from itemloaders.processors import TakeFirst


class ItalycaindosuezSpider(scrapy.Spider):
	name = 'italycaindosuez'
	start_urls = ['https://italy.ca-indosuez.com/in-prima-pagina/news']

	def parse(self, response):
		post_links = response.xpath('//a[@class="block-article--link"]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//div[@class="listeNews__more-articles ml-10"]/a/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//div[@class="block-articleTitle--title mb-30"]/h3/text()').get()
		description = response.xpath('//div[@class="block-wysiwg-text"]/p/text()[normalize-space()]|//div[@class="block-articleTitle--description"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//p[@class="fs-15 lh-25 p-0 m-0 color-shark"]/text()').get()

		item = ItemLoader(item=ItalycaindosuezItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
