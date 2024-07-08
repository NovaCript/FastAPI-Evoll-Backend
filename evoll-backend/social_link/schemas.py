from pydantic import BaseModel, ConfigDict, HttpUrl


class SocialLinkBase(BaseModel):
    social_network: str
    link: HttpUrl


class SocialLinkCreate(SocialLinkBase):
    pass


class SocialLinkRead(SocialLinkBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    user_id: int


class SocialLinkUpdate(SocialLinkCreate):
    pass


class SocialLinkUpdatePartial(SocialLinkCreate):
    social_network: str | None = None
    link: HttpUrl | None = None
    