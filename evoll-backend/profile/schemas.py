from enum import Enum
from typing import Optional

from pydantic.json_schema import SkipJsonSchema
from pydantic import BaseModel, Field
from pydantic import ConfigDict
from datetime import date


class RoleUser(str, Enum):
    athlete = "athlete"
    sponsor = "sponsor"
    club = "club"


class ProfileCount(BaseModel):
    count: int

class ProfileBase(BaseModel):
    first_name: str | None
    last_name: str | None
    gender: str | None
    date_of_birth: date | None
    user_id: int
    country_id: int


class ProfileCreate(ProfileBase):
    pass


class ProfileRead(ProfileBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int


class ProfileUpdate(ProfileBase):
    user_id: SkipJsonSchema[int] = Field('user_id', exclude=True)
    country_id: SkipJsonSchema[int] = Field('country_id', exclude=True)


class ProfileUpdatePartial(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    gender: str | None = None
    date_of_birth: date | None = None


class ProfileSearchRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    role: Optional[RoleUser] = None
    