from .base import Base
from sqlalchemy import Column, Integer, DateTime, String, Float

class StockTransaction(Base):
    __tablename__ = "StockTransaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    date = Column(DateTime)
    last_price = Column(Integer)
    max_price = Column(Integer)
    min_price = Column(Integer)    
    avg_price = Column(Float)
    cash_flow_per = Column(Float)
    amount = Column(Integer)
    cash_flow = Column(Integer)