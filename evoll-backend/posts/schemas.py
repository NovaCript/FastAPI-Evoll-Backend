from pydantic import BaseModel
from pydantic import ConfigDict


class PostsBase(BaseModel):
    title: str | None
    body: str | None
    user_id: int


class PostsCreate(PostsBase):
    pass


class PostsRead(PostsBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
