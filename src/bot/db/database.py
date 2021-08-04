import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASS = os.environ.get('POSTGRES_PASSWORD')

engine = create_engine(
    f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@db:5432/{DB_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()
