import scrapy
from ..utils import get_start_date
from datetime import datetime
from ..config import Session
from ..models import StockTransaction
from scrapy.http import Response,FormRequest

class StockSpider(scrapy.Spider):
    name = 'stock-spider'

    codes_url = "https://www.mse.mk/mk/stats/symbolhistory/KMB"

    def __init__(self):
        self.codes = []
        self.transactions = []
        self.session = Session()

    def start_requests(self):
        yield scrapy.Request(self.codes_url, callback=self.parse_codes) 
    
    def parse_codes(self, response: Response):
        self.codes = [code for code in response.xpath("//select[@id='Code']/option/text()").getall() if not any(char.isdigit() for char in code)]

        for code in self.codes:
            from_date, to_date = get_start_date(code,self.session)
            for year in range(from_date.year, to_date.year+1):
                f = from_date.replace(year=year).strftime("%d.%m.%Y")
                t = to_date.replace(year=year+1).strftime("%d.%m.%Y") if year != to_date.year else to_date.strftime("%d.%m.%Y")

                formdata = {
                    "FromDate":f,
                    "ToDate":t,
                    "Code":code
                }
                
                yield FormRequest(
                    url = response.url,
                    formdata=formdata,
                    callback=self.parse,
                    meta={"code":code}
                )
            

    def parse(self, response: Response):
        code = response.meta.get('code')

        rows = response.xpath("//table[@id='resultsTable']/tbody/tr")
        for row in rows:
            values  = [td.xpath(".//text()").get() for td in row.xpath(".//td")]
            model = StockTransaction(
            code = code,
            date = datetime.strptime(values[0],"%d.%m.%Y"),
            last_transaction = values[1] if values[1] else '0',
            max_transaction = values[2] if values[2] else '0',
            min_transaction = values[3] if values[3] else '0',
            avg_transaction = values[4] if values[4] else '0',
            cash_flow_per = values[5] if values[5] else '0',
            quantity = values[6] if values[6] else '0',
            cash_flow = values[8] if values[8] else '0'
            )
        
            self.transactions.append(model)
    
    def closed(self,reason):
       self.session.bulk_save_objects(self.transactions)
       self.session.commit()
       self.session.close