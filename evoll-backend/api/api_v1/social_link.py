from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from utils.raise_http_exception import ex
from core.models import db_helper, SocialLink
from social_link.schemas import (
    SocialLinkCreate, 
    SocialLinkRead, 
    SocialLinkUpdate, 
    SocialLinkUpdatePartial
)
from core.models import User
from auth.validation_auth import get_current_auth_active_user
from social_link import crud 
from social_link.depends import get_social_link_by_current_user


router = APIRouter(tags=['Social_link'])


@router.get('/{social_link_id}', response_model=SocialLinkRead)
async def get_social_link(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    social_link_id: int,
):
    social_link = await crud.get_social_link_by_id(
        session=session, 
        social_link_id=social_link_id
    )
    if not social_link:
        raise ex.social_link_not_found()
    return social_link
    


@router.get('', response_model=list[SocialLinkRead])
async def get_social_links(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_id: int | None = None
):
    return await crud.get_all_social_links(
        session=session,
        user_id=user_id,
    )


@router.post('', response_model=SocialLinkCreate)
async def create_link(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ], 
    social_link: SocialLinkCreate,
    user: User = Depends(get_current_auth_active_user),
):
    return await crud.create_social_link(
        session=session, 
        social_link=social_link, 
        user=user)


@router.put('/{social_link_id}', response_model=SocialLinkRead)
async def update_social_link(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    social_link_update: SocialLinkUpdate,
    social_link: SocialLink = Depends(get_social_link_by_current_user)
):  
    social_link_changed = await crud.social_link_update(
        session=session,
        social_link=social_link,
        social_link_update=social_link_update,
    )
    return social_link_changed


@router.patch('/{social_link_id}', response_model=SocialLinkRead)
async def partial_update_social_link(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    social_link_update: SocialLinkUpdatePartial,
    social_link: SocialLink = Depends(get_social_link_by_current_user)
):  
    social_link_changed = await crud.social_link_update(
        session=session,
        social_link=social_link,
        social_link_update=social_link_update,
        partial=True
    )
    return social_link_changed


@router.delete('/{social_link_id}', response_model=None)
async def delete_social_link(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    social_link: SocialLink = Depends(get_social_link_by_current_user)
):
    social_link = await crud.social_link_delete(
        session=session,
        social_link=social_link,
    )
