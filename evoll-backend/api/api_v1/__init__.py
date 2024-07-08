from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.config import settings

from api.api_v1.users import router as users_router
from api.api_v1.profile import router as profile_router
from api.api_v1.country import router as country_router
from api.api_v1.auth import router as auth_router
from api.api_v1.social_link import router as social_link_router

http_bearer = HTTPBearer(auto_error=False)


router = APIRouter(
    prefix=settings.api.v1.prefix,

)
router.include_router(
    users_router,
    prefix=settings.api.v1.users,
)
router.include_router(
    profile_router,
    prefix=settings.api.v1.profile,
)

router.include_router(
    country_router,
    prefix=settings.api.v1.country,
)

router.include_router(
    auth_router,
    prefix=settings.api.v1.auth,
)

router.include_router(
    social_link_router,
    prefix=settings.api.v1.social_link,
)