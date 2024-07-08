from typing import Sequence

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from profile.models import Profile
from profile.schemas import ProfileUpdate, ProfileUpdatePartial


async def get_all_profile(
    session: AsyncSession,
    offset: int,
    limit: int,
) -> Sequence[Profile]:
    stmt = select(Profile).order_by(Profile.id).offset(offset).limit(limit)
    result = await session.scalars(stmt)
    return result.all()


async def get_profile_by_user_id(
        session: AsyncSession,
        user_id: int,
) -> Profile | None:
    stmt = select(Profile).where(Profile.user_id == user_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def get_profile_by_id(
    session: AsyncSession,
    profile_id: int,
) -> Profile | None:
    stmt = select(Profile).where(Profile.id == profile_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def update_profile(
        session: AsyncSession,
        profile: Profile, 
        profile_update: ProfileUpdate | ProfileUpdatePartial,
        partial: bool = False
) -> Profile:
    for name, value in profile_update.model_dump(exclude_unset=partial).items():
        setattr(profile, name, value)
    await session.commit()
    await session.refresh(profile)
    return profile


async def search_profile(
    session: AsyncSession,
    first_name: str | None = None,
    last_name: str | None = None,
    country: str | None = None,
    region: str | None = None,
    role: str | None = None,
) -> Sequence[Profile]:

    stmt = select(Profile).options(
        selectinload(Profile.country), selectinload(Profile.user)
    )
    if first_name:
        stmt = stmt.where(Profile.first_name.ilike(f"%{first_name}%"))
    if last_name:
        stmt = stmt.where(Profile.last_name.ilike(f"%{last_name}%"))
    if country:
        stmt = stmt.where(Profile.country.has(country_name=country))
    if region:
        stmt = stmt.where(Profile.country.has(region=region))
    if role:
        stmt = stmt.where(Profile.user.has(role=role))

    result = await session.scalars(stmt)
    return result.all()


async def get_count_profile(
        session: AsyncSession,
) -> int:
    stmt = select(func.count(Profile.id))
    result = await session.execute(stmt)
    return result.scalar_one()
