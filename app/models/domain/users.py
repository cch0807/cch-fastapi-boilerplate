from sqlalchemy import Column, String
from app.db.base_class import Base

from app.models.common import DateTimeModelMixin, IDModelMixin


class Users(IDModelMixin, DateTimeModelMixin, Base):
    __tablename__ = "users"
    nickname = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False, unique=True, index=True)
