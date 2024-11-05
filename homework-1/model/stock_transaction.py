from .base import Base
from sqlalchemy import Column, Integer, DateTime, String, Numeric, Float

class StockTransaction(Base):
    __tablename__ = "StockTransaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    date = Column(DateTime)
    last_price = Column(String)
    max_price = Column(String)
    min_price = Column(String)    
    avg_price = Column(String)
    cash_flow_per = Column(String)
    amount = Column(String)
    cash_flow = Column(String)