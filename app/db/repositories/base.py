from fastapi import Depends

from sqlalchemy.orm import Session
from app.db.connection import get_db


class BaseRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session
