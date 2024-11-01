import requests
from model import Base
from config import engine
from datetime import datetime
from bs4 import BeautifulSoup
from utils import get_codes, get_start_date

def get_transactions(codes):

    transactions = []
    for code in codes:

        from_date = get_start_date(code)
        data = requests.post("https://www.mse.mk/mk/stats/symbolhistory/REPL",{
            "FromDate":from_date.strftime("%d.%m.%Y"),
            "ToDate":datetime.now().strftime("%d.%m.%Y"),
            "Code":code
        })

        print(f'Getting transactions for {code} from date {from_date} til now!')

        bs = BeautifulSoup(data.text,"html.parser")
        rows = bs.find("table",{"id":"resultsTable"}).find("tbody").find_all("tr")
        
        for row in rows:
            values = row.text.strip().split("\n")
            transaction = (
                    code,
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4],
                    values[5],
                    values[6],
                    values[8]
                )
            transactions.append(transaction)
            
    return transaction

def get_data():
     codes = get_codes()
     transactions = get_transactions(codes=codes)
     return transactions