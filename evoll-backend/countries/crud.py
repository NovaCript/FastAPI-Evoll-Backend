from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from countries.models import Country


async def get_all_country(
    session: AsyncSession,
) -> Sequence[Country]:
    stmt = select(Country).order_by(Country.region)
    result = await session.scalars(stmt)
    return result.all()


async def get_country_by_id(
    session: AsyncSession,
    country_id: int,
) -> Country | None:
    stmt = select(Country).where(Country.id == country_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()
