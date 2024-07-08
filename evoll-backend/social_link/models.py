from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin
from core.models.mixins.user_relation import UserRelationMixin

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, validates


class SocialLink(IntIdPkMixin, UserRelationMixin, Base):
    _user_back_populates = 'social_link'

    social_network: Mapped[str] = mapped_column(String(55))
    link: Mapped[str] = mapped_column(String(255))
    
    @validates('link')
    def validate_link(self, key, value):
        return str(value)
    