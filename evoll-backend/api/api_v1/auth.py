from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from auth.helpers import create_access_token, create_refresh_token
from auth.schemas import TokenInfo
from auth.validation_auth import (
    get_current_auth_user_for_refresh,
)
from core.models import db_helper
from users.schemas import UserLogin, UserRead, UserCreate
from users import crud as user_crud
from utils.raise_http_exception import ex
from users.user_manager import utils as user_manager
from users import crud as users_crud
from countries import crud as country_crud
from auth.validation_auth import validate_password

router = APIRouter(tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=201)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_create: UserCreate,
):
    if user_create.password != user_create.re_password:
        raise ex.passwords_do_not_match()

    if not user_create.user_agreement:
        raise ex.must_agree_to_user_agreement()

    user = await users_crud.get_user_by_username(
        session=session,
        username=user_create.username,
    )
    if user:
        raise ex.already_taken()

    email = await users_crud.get_user_by_email(
        session=session,
        email=user_create.email,
    )
    if email:
        raise ex.email_already_taken()

    country = await country_crud.get_country_by_id(
        session=session,
        country_id=user_create.country_id,
    )
    if not country:
        raise ex.country_not_found()

    user = await user_manager.create_user(
        session=session,
        user_create=user_create,
    )

    await user_manager.create_user_profile(
        session=session,
        user_id=user.id,
        country_id=user_create.country_id,
    )
    return user


@router.post("/login", response_model=TokenInfo)
async def auth_user_jwt(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_login: UserLogin,
):
    user = await user_crud.get_user_by_username(session=session, username=user_login.username)
    if not user:
        raise ex.unauthorized()
    if not await validate_password(password=user_login.password, hash_password=user.password_hash):
        raise ex.unauthorized()
    if not user.is_active:
        raise ex.inactive_user()
    access_token = await create_access_token(user=user)
    refresh_token = await create_refresh_token(user=user)
    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post(
    "/refresh",
    response_model=TokenInfo,
    response_model_exclude_none=True,
)
async def auth_user_refresh(
    user: UserRead = Depends(get_current_auth_user_for_refresh),
):
    access_token = await create_access_token(user=user)
    return TokenInfo(
        access_token=access_token,
    )

