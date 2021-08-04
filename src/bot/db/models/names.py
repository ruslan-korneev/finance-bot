from sqlalchemy import Column, Integer, String
from db.database import Base


class NameIncome(Base):
    __tablename__ = 'income_names'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class NameExpense(Base):
    __tablename__ = 'expense_names'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
