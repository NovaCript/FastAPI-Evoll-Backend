import bcrypt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from jwt import InvalidTokenError

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper
from users import crud as users_crud

from auth import utils as auth_utils
from users.schemas import UserRead
from utils.raise_http_exception import ex
from auth.helpers import (
    TOKEN_TYPE_FIELD,
    ACCESS_TOKEN_TYPE,
    REFRESH_TOKEN_TYPE,
)
from fastapi.security import HTTPBearer

http_bearer = HTTPBearer(auto_error=False)


async def get_current_token_payload(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> dict:
    if not credentials:
        raise ex.token_invalid()
    token = credentials.credentials
    try:
        payload = await auth_utils.decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise ex.token_invalid()
    return payload


async def validate_token_type(
    payload: dict,
    token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise ex.invalid_token_type(current_token_type, token_type)


async def get_user_by_token_sub(payload: dict, session: AsyncSession):
    user_id = payload.get("sub")
    user = await users_crud.get_user_by_id(session, id=user_id)
    if not user:
        raise ex.token_invalid()
    return user


class UserGetterFromToken:
    def __init__(self, token_type: str):
        self.token_type = token_type

    async def __call__(
        self,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        payload: dict = Depends(get_current_token_payload),
    ):
        await validate_token_type(payload, self.token_type)
        return await get_user_by_token_sub(session=session, payload=payload)


get_current_auth_user = UserGetterFromToken(ACCESS_TOKEN_TYPE)
get_current_auth_user_for_refresh = UserGetterFromToken(REFRESH_TOKEN_TYPE)

async def get_current_auth_active_user(
        user: UserRead = Depends(get_current_auth_user)
):
    if user.is_active:
        return user
    raise ex.inactive_user()

async def hash_password(
        password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd: bytes = password.encode()
    return bcrypt.hashpw(pwd, salt)

# validate password
async def validate_password(
        password: str,
        hash_password: bytes,
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hash_password,
    )