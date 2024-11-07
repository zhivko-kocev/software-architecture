from .base import Base
from sqlalchemy import Column, Integer, DateTime, String

class StockTransaction(Base):
    __tablename__ = "StockTransaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    date = Column(DateTime)
    last_transaction = Column(String)
    max_transaction = Column(String)
    min_transaction = Column(String)    
    avg_transaction = Column(String)
    cash_flow_per = Column(String)
    quantity = Column(String)
    cash_flow = Column(String)