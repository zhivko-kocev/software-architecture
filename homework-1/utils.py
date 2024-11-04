from bs4 import BeautifulSoup
from config import Session
from model import StockTransaction
from datetime import datetime

def get_transactions(codes, session):
    
    transactions = []

    for code in codes:

        from_date, today = get_start_date(code)

        if from_date.date() >= today.date():
            continue

        for year in range(from_date.year, today.year+1):
            
            f = from_date.replace(year=year).strftime("%d.%m.%Y")
            t =  today.replace(year=year+1).strftime("%d.%m.%Y") if year != today.year else today.strftime("%d.%m.%Y")

            data = session.post("https://www.mse.mk/mk/stats/symbolhistory/REPL",data={
                  "FromDate":f,
                  "ToDate":t,
                  "Code":code
            })

            table = BeautifulSoup(data.text,"html.parser").find("table",{"id":"resultsTable"})

            if not table:
                continue

            rows = table.find("tbody").find_all("tr")
        
            for row in rows:
                values = row.text.strip().split("\n")
                transaction = (
                        code,
                        datetime.strptime(values[0],"%d.%m.%Y") if values[0] else None,
                        values[1] if values[1] else None,
                        values[2] if values[2] else None,
                        values[3] if values[3] else None,
                        values[4] if values[4] else None,
                        values[5] if values[5] else None,
                        values[6] if values[6] else None,
                        values[8] if values[8] else None
                    )
                
                transactions.append(transaction)

    return transactions

def get_start_date(code):
     session = Session()

     last_scraped = session.query(StockTransaction)\
            .filter(StockTransaction.code == code)\
            .order_by(StockTransaction.date.desc()).first()
     
     session.close()

     
     today = datetime.today()
        
     if not last_scraped:
        from_date = today.replace(year=today.year-10,day=today.day+1)
     else:
        from_date = last_scraped.date.replace(day=last_scraped.date.day+1)
        

     return from_date,today

def get_codes(session):

    site = session.get("https://www.mse.mk/mk/stats/symbolhistory/REPL")
    bs = BeautifulSoup(site.text,"html.parser")

    codes = bs.find("select",{"id":"Code"}).find_all("option")
    codes = [code.text for code in codes if not any(char.isdigit() for char in code.text)]
    
    return codes
