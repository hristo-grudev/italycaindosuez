BOT_NAME = 'italycaindosuez'

SPIDER_MODULES = ['italycaindosuez.spiders']
NEWSPIDER_MODULE = 'italycaindosuez.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'italycaindosuez.pipelines.ItalycaindosuezPipeline': 100,

}