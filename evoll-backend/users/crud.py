from typing import Sequence
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User


async def get_all_users(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User | None:
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    return user


async def get_user_by_email(
    session: AsyncSession,
    email: str,
) -> User | None:
    stmt = select(User).where(User.email == email)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    return user




async def get_user_by_id(
    session: AsyncSession,
    id: int,
) -> User | None:
    stmt = select(User).where(User.id == id)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    return user


