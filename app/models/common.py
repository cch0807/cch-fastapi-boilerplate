from sqlalchemy import BigInteger, Column, DateTime, func
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=func.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


class IDModelMixin:
    @declared_attr
    def id(cls):
        return Column(BigInteger, primary_key=True, index=True, autoincrement=True)
