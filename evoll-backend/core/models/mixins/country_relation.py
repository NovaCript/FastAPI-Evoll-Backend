from sqlalchemy.orm import declared_attr, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from countries.models import Country


class CountryRelationMixin:
    _country_id_nullable: bool = False
    _country_id_unique: bool = False
    _country_back_populates: str | None = None

    @declared_attr
    def country_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("countries.id"),
            unique=cls._country_id_unique,
            nullable=cls._country_id_nullable,
        )

    @declared_attr
    def country(cls) -> Mapped["Country"]:
        return relationship(
            "Country",
            back_populates=cls._country_back_populates,
        )
