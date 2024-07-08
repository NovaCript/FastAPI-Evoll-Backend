from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from auth.validation_auth import get_current_token_payload, \
    get_current_auth_active_user
from core.models import db_helper
from users.models import User
from users.schemas import (
    UserRead,
)

from utils.raise_http_exception import ex

from users import crud as users_crud

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    users = await users_crud.get_all_users(session=session)
    return users


@router.get("/", response_model=UserRead)
async def get_user_by_username(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    username: str,
):
    user = await users_crud.get_user_by_username(
        session=session,
        username=username,
    )
    if not user:
        raise ex.user_not_found(username)
    return user

@router.get("/me")
async def auth_user_check(
    payload: dict = Depends(get_current_token_payload),
    user: User = Depends(get_current_auth_active_user),
) -> dict:
    iat = payload.get("iat")
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "logged_at": iat
    }