# import os
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("DATABASE_URL")
engine = create_engine(url if url else 'sqlite:///stockmarket/database/stock.db')
Session = sessionmaker(bind=engine)