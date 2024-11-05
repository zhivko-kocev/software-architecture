import time
import requests
import pandas as pd
from model import Base
from config import engine
from utils import get_codes, write_transactions

if __name__ == "__main__":

    #create all models
    Base.metadata.create_all(engine)

    #start the session
    http_session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    http_session.mount('https://', adapter)

    #get the codes of the stock market
    codes = get_codes(http_session=http_session)

    #start counting
    start = time.perf_counter()
    
    #get and write the scraped data
    write_transactions(codes=codes,http_session=http_session)
    
    #finish counting
    end = time.perf_counter()
    print(f'The extraction and the writing took {end - start:.3f}s')

    #close the session
    http_session.close()

