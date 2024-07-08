"""create country table

Revision ID: f10a81e60818
Revises: 4fd3eb31b4e6
Create Date: 2024-06-09 15:28:10.793110

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f10a81e60818"
down_revision: Union[str, None] = "4fd3eb31b4e6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "countries",
        sa.Column("country_name", sa.String(length=40), nullable=False),
        sa.Column("region", sa.String(length=40), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_countries")),
    )


def downgrade() -> None:
    op.drop_table("countries")
