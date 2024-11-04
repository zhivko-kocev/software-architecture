import time
import pandas as pd
from crawler import get_transactions
from model import Base
from config import engine

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    start = time.perf_counter()
    data = get_transactions()
    df = pd.DataFrame(data,columns=["code","date","last_price","max_price","min_price","avg_price","cash_flow_per","amount","cash_flow"])
    df.fillna(0, inplace=True)
    df.to_sql('StockTransaction', con=engine, if_exists='append', index=False)
    end = time.perf_counter()
    print(f'The extraction and the writing took {end - start:.3f}s')
