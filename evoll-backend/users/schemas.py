from enum import Enum

from pydantic import BaseModel
from pydantic import ConfigDict, EmailStr

from profile.schemas import ProfileRead
from posts.schemas import PostsRead

class RoleUser(str, Enum):
    athlete = "athlete"
    sponsor = "sponsor"
    club = "club"


class UserBase(BaseModel):
    username: str


class UserLogin(UserBase):
    password: str


class UserCreate(UserBase):
    model_config = ConfigDict(use_enum_values=True)
    email: EmailStr
    password: str
    re_password: str
    role: RoleUser
    user_agreement: bool = True
    country_id: int



class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int


class UserProfile(UserRead):
    profile: ProfileRead


class UserPosts(UserRead):
    posts: list[PostsRead]
