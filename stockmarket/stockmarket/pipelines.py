# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from stockmarket.config import  Session
from stockmarket.models.stock_transaction import StockTransaction

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StockmarketPipeline:

    def __init__(self) -> None:
        self.transactions = []
    
    def close_spider(self,spider):
        session = Session()
        session.bulk_save_objects(self.transactions)
        session.commit()
        session.close()
        
    def process_item(self, item, spider):
        
        model = StockTransaction(
            code = item['code'],
            date = item['date'],
            last_transaction = item['last_transaction'],
            max_transaction = item['max_transaction'],
            min_transaction = item['min_transaction'],
            avg_transaction = item['avg_transaction'],
            cash_flow_per = item['cash_flow_per'],
            quantity = item['quantity'],
            cash_flow = item['cash_flow']
        )
        
        self.transactions.append(model)

        return item
