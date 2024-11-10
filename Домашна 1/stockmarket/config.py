import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
url = os.getenv("DATABASE_URL")
engine = create_engine(url if url else "sqlite:///stockmarket/database/stock.db")
Session = sessionmaker(bind=engine)
