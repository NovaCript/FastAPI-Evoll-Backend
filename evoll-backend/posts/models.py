from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Text

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin
from core.models.mixins.user_relation import UserRelationMixin


class Post(IntIdPkMixin, UserRelationMixin, Base):
    # _user_id_nullable = False
    # _user_id_unique = False
    _user_back_populates = "posts"

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
