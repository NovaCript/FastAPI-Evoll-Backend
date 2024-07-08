from typing import Annotated

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User, SocialLink
from auth.validation_auth import get_current_auth_active_user
from social_link import crud

from utils.raise_http_exception import ex


async def get_social_link_by_current_user(
    social_link_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
    current_user: User = Depends(get_current_auth_active_user),
) -> SocialLink | None:
    social_link = await crud.get_social_link_by_id(
        session=session,
        social_link_id=social_link_id,
    )
    if not social_link:
        raise ex.social_link_not_found()
    
    if social_link.user_id != current_user.id:
        raise ex.forbidden()
    
    return social_link
