from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from db.database import Base
from db.models.names import NameExpense


class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    name = relationship(NameExpense, secondary='expenses_name')
    amount = Column(Float)
    currency = Column(String(255))
    date_expense = Column(DateTime)


class ExpensesName(Base):
    __tablename__ = 'expenses_name'
    id = Column(Integer, primary_key=True)
    expense_id = Column(Integer, ForeignKey('expenses.id'), primary_key=True)
    nameexpense_id = Column(Integer, ForeignKey('expense_names.id'),
                            primary_key=True) 
