from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Sequence

from social_link.models import SocialLink
from social_link.schemas import SocialLinkCreate, SocialLinkUpdate, SocialLinkUpdatePartial
from core.models import User
from sqlalchemy.exc import NoResultFound
from utils.raise_http_exception import ex


async def create_social_link(
    session: AsyncSession,
    social_link: SocialLinkCreate,
    user: User
) -> SocialLink:  
    social_link = SocialLink(**social_link.model_dump(), user_id=user.id)
    session.add(social_link)
    await session.commit()
    return social_link


async def get_social_link_by_id(
    session: AsyncSession,
    social_link_id: int,
) -> SocialLink:
    stmt = select(SocialLink).where(SocialLink.id == social_link_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def get_all_social_links(
    session: AsyncSession,
    user_id: int | None = None
) -> Sequence[SocialLink]:
    stmt = select(SocialLink).order_by(SocialLink.id)
    if user_id:
        stmt = stmt.where(SocialLink.user_id == user_id)
    result = await session.scalars(stmt)
    return result.all()


async def social_link_update(
    session: AsyncSession,
    social_link: SocialLink,
    social_link_update: SocialLinkUpdate | SocialLinkUpdatePartial,
    partial: bool =  False
) -> SocialLink:

    for name, value in social_link_update.model_dump(exclude_unset=partial).items():
        setattr(social_link, name, value)

    await session.commit()
    return social_link


async def social_link_delete(
    session: AsyncSession,
    social_link: SocialLink
) -> None:
    await session.delete(social_link)
    await session.commit()
