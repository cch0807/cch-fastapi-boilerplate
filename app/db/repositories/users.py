from sqlalchemy import select
from app.db.repositories.base import BaseRepository
from app.models.domain.users import Users


class UserRepository(BaseRepository):
    async def get_user_by_username(self, username: str) -> Users | None:
        return self.session.scalar(
            select(Users).where(
                Users.nickname,
            )
        )
