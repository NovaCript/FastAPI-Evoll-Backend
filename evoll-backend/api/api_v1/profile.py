from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from profile.schemas import (
    ProfileRead,
    ProfileSearchRequest,
    ProfileCount,
    ProfileUpdate,
    ProfileUpdatePartial
)

from profile.models import Profile
from profile.depends import get_profile_by_current_user
from profile import crud as profile_crud
from utils.raise_http_exception import ex


router = APIRouter(
    tags=["Profile"],
)


@router.get("", response_model=list[ProfileRead])
async def get_profile(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    limit: int = 10,
    offset: int = 0,
):
    profile = await profile_crud.get_all_profile(session=session, limit=limit, offset=offset)
    return profile


@router.get("/me", response_model=ProfileRead)
async def get_my_profile(
        profile: Profile = Depends(get_profile_by_current_user),
):
    if not profile:
        raise ex.profile_not_found()
    return profile


@router.put("/me", response_model=ProfileRead)
async def update_profile(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        profile_update: ProfileUpdate,
        profile: Profile = Depends(get_profile_by_current_user),
): 
    if not profile:
        raise ex.profile_not_found()
    changed_profile = await profile_crud.update_profile(
        session=session,
        profile_update=profile_update,
        profile=profile,
    )   
    return changed_profile


@router.patch("/me", response_model=ProfileRead)
async def partial_update_profile(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        profile_update: ProfileUpdatePartial,
        profile: Profile = Depends(get_profile_by_current_user),
):
    if not profile:
        raise ex.profile_not_found()
    changed_profile = await profile_crud.update_profile(
        session=session,
        profile_update=profile_update,
        profile=profile,
        partial=True,
    )
    return changed_profile


@router.get("/count_profile", status_code=200, response_model=ProfileCount)
async def get_count_profile(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    count = await profile_crud.get_count_profile(session=session)
    return {"count": count}


@router.get("/{profile_id}", response_model=ProfileRead)
async def get_profile_by_id(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    profile_id: int,
):
    profile = await profile_crud.get_profile_by_id(
        session=session,
        profile_id=profile_id,
    )
    if not profile:
        raise ex.profile_not_found()
    return profile


@router.get("/search/", response_model=list[ProfileRead])
async def search_profile(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    search_request: Annotated[
        ProfileSearchRequest,
        Depends(),
    ],
):
    profile = await profile_crud.search_profile(
        session=session,
        first_name=search_request.first_name,
        last_name=search_request.last_name,
        country=search_request.country,
        region=search_request.region,
        role=search_request.role,
    )
    return profile

