from datetime import datetime
from .models import StockTransaction

def get_start_date(code,session):

     last_scraped = session.query(StockTransaction)\
            .filter(StockTransaction.code == code)\
            .order_by(StockTransaction.date.desc()).first()
     
     today = datetime.today()
        
     if not last_scraped:
        from_date = today.replace(year=today.year-10,day=today.day+1)
     else:
        from_date = last_scraped.date.replace(day=last_scraped.date.day+1)
        

     return from_date,today