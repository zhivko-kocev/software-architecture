import time
import pandas as pd
from crawler import get_data
from model import Base
from config import engine

if __name__ == "__main__":
    start = time.perf_counter()
    Base.metadata.create_all(engine)
    data = get_data()
    end = time.perf_counter()
    time_duration = end - start
    print(f'The extraction and the writing took {time_duration:.3f}s')
