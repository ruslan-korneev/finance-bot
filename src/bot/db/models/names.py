from sqlalchemy import Column, Integer, String
from db.database import Base


class Name(Base):
    __tablename__ = 'names'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
