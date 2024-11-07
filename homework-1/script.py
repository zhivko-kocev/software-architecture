from stockmarket.models import Base
from stockmarket.config import engine
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from stockmarket.spiders.stock_spider import StockSpider


if __name__ == "__main__":
    
    Base.metadata.create_all(engine)

    process = CrawlerProcess(get_project_settings())
    process.crawl(StockSpider)
    process.start()