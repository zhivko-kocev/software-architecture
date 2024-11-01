import requests
from bs4 import BeautifulSoup
from config import Session
from model import StockTransaction
from datetime import datetime, timedelta

def get_start_date(code):
     session = Session()

     last_scraped = session.query(StockTransaction)\
            .filter(StockTransaction.code == code)\
            .order_by(StockTransaction.date.desc()).first()
        
     if not last_scraped:
        from_date = datetime.now() - timedelta(days=365 * 10)
     else:
        from_date = last_scraped.date + timedelta(days=1)
        
     session.close()

     return from_date

def get_codes():

    site = requests.get("https://www.mse.mk/mk/stats/symbolhistory/REPL")
    bs = BeautifulSoup(site.text,"html.parser")

    codes = bs.find("select",{"id":"Code"}).find_all("option")
    codes = [code.text for code in codes if not any(char.isdigit() for char in code.text)]
    
    return codes
