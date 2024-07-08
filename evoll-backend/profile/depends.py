from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Profile, User
from auth.validation_auth import get_current_auth_active_user
from profile.crud import get_profile_by_user_id


async def get_profile_by_current_user(
    user: User = Depends(get_current_auth_active_user),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Profile:
    profile = await get_profile_by_user_id(user_id=user.id, session=session)
    return profile
