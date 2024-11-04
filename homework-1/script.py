import time
import requests
import pandas as pd
from model import Base
from config import engine
from utils import get_codes, get_transactions

if __name__ == "__main__":

    #create all models
    Base.metadata.create_all(engine)

    #start the session
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    session.mount('https://', adapter)

    #get the codes of the stock market
    codes = get_codes(session=session)

    #start counting
    start = time.perf_counter()
    
    #get the scraped data
    data = get_transactions(codes,session)

    #prepare and insert to database
    df = pd.DataFrame(data,columns=["code","date","last_price","max_price","min_price","avg_price","cash_flow_per","amount","cash_flow"])
    df.fillna(0, inplace=True)
    df.to_sql('StockTransaction', con=engine, if_exists='append', index=False)
    
    #finish counting
    end = time.perf_counter()
    print(f'The extraction and the writing took {end - start:.3f}s')

    #close the session
    session.close()

