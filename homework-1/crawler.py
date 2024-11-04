import requests
from datetime import datetime
from bs4 import BeautifulSoup
from utils import get_codes, get_start_date

def get_transactions():

    transactions = []
    codes = get_codes()

    for code in codes:

        from_date = get_start_date(code)
        today = datetime.now()

        if from_date.date() == today.date():
            continue

        data = requests.post("https://www.mse.mk/mk/stats/symbolhistory/REPL",{
            "FromDate":from_date.strftime("%d.%m.%Y"),
            "ToDate":today.strftime("%d.%m.%Y"),
            "Code":code
        })

        table = BeautifulSoup(data.text,"html.parser").find("table",{"id":"resultsTable"})

        if not table:
            continue
        
        print(f'Getting transactions for {code} from date {from_date} til now!')

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