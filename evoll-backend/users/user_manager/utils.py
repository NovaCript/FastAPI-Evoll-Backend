from datetime import date
from auth.validation_auth import hash_password
from sqlalchemy.ext.asyncio import AsyncSession
from profile.models import Profile
from users.models import User
from users.schemas import UserCreate



async def create_user(
        session: AsyncSession,
        user_create: UserCreate,
):
    user_data = user_create.dict(exclude={"password", "re_password", "country_id"})
    user = User(**user_data)
    user.password_hash = await hash_password(user_create.password)

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def create_user_profile(
    session: AsyncSession,
    user_id: int,
    country_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    gender: str | None = None,
    date_of_birth: date | None = None,
) -> Profile:
    profile = Profile(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        date_of_birth=date_of_birth,
        user_id=user_id,
        country_id=country_id,
    )
    session.add(profile)
    await session.commit()
    await session.refresh(profile)
    return profile
