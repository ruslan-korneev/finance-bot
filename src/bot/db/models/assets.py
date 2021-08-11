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
from db.models.names import NameAsset


class Asset(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    name = relationship(NameAsset, secondary='assets_name')
    amount = Column(Float)
    currency = Column(String(255))
    date_purchase = Column(DateTime)


class AssetsName(Base):
    __tablename__ = 'assets_name'
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('assets.id'), primary_key=True)
    nameasset_id = Column(Integer, ForeignKey('asset_names.id'),
                            primary_key=True)
