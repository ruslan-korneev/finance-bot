from sqlalchemy import ForeignKey, Integer, String, Column, DateTime, Float
from sqlalchemy.orm import relationship
from db.database import Base
from db.models.names import NameIncome


class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key = True)
    name = relationship(NameIncome, secondary='incomes_name')
    amount = Column(Float)
    currency = Column(String(255))
    date_income = Column(DateTime)

class IncomesName(Base):
    __tablename__ = 'incomes_name'
    id = Column(Integer, primary_key=True)
    income_id = Column(Integer, ForeignKey('incomes.id'), primary_key=True)
    nameincome_id = Column(Integer, ForeignKey('income_names.id'),
                           primary_key=True)
