from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String
from sqlalchemy import func
from datetime import datetime

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from posts.models import Post

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    password_hash: Mapped[bytes]
    email: Mapped[str] = mapped_column(String(255), unique=True)
    role: Mapped[str] = mapped_column(String(32))
    user_agreement: Mapped[bool] = mapped_column(default=True)  # change to False
    is_active: Mapped[bool] = mapped_column(default=True)
    date_register: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )

    # posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")
    social_link: Mapped[list["SocialLink"]] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)
