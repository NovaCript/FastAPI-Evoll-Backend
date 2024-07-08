from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Date

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin
from core.models.mixins.user_relation import UserRelationMixin
from core.models.mixins.country_relation import CountryRelationMixin


class Profile(IntIdPkMixin, UserRelationMixin, CountryRelationMixin, Base):
    # user_id
    # _user_id_nullable = False
    _user_id_unique = True
    _user_back_populates = "profile"

    # country_id
    # _country_id_nullable: bool = False
    # _country_id_unique: bool = False
    _country_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    gender: Mapped[str | None] = mapped_column(String(100))
    date_of_birth: Mapped[Date | None] = mapped_column(Date)
