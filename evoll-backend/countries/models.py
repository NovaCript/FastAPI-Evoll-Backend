from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from profile.models import Profile


class Country(IntIdPkMixin, Base):
    __tablename__ = "countries"

    country_name: Mapped[str] = mapped_column(String(40))
    region: Mapped[str] = mapped_column(String(40))

    profile: Mapped[list["Profile"]] = relationship(back_populates="country")
