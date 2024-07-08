from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from countries.schemas import (
    CountryRead,
)

from countries import crud as country_crud

from utils.raise_http_exception import ex

router = APIRouter(
    tags=["Countries"],
)


@router.get("", response_model=list[CountryRead])
async def get_country(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    country = await country_crud.get_all_country(
        session=session,
    )
    return country
