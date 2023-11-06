from pathlib import Path

SPIDER_NAME = 'pep'
ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://peps.python.org/']
BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}
PIPELINE_PRIORITY = 300
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': PIPELINE_PRIORITY,
}
