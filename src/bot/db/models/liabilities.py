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
from db.models.names import NameLiability


class Liability(Base):
    __tablename__ = 'liabilities'
    id = Column(Integer, primary_key=True)
    name = relationship(NameLiability, secondary='liabilities_name')
    amount = Column(Float)
    currency = Column(String(255))
    date_purchase = Column(DateTime)


class LiabilitiesName(Base):
    __tablename__ = 'liabilities_name'
    id = Column(Integer, primary_key=True)
    liability_id = Column(Integer, ForeignKey('liabilities.id'), primary_key=True)
    nameliability_id = Column(Integer, ForeignKey('liability_names.id'),
                            primary_key=True)
