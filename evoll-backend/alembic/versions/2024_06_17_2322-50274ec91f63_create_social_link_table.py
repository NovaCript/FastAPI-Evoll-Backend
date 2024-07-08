"""create social_link table

Revision ID: 50274ec91f63
Revises: 02832325b3ea
Create Date: 2024-06-17 23:22:29.800826

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "50274ec91f63"
down_revision: Union[str, None] = "02832325b3ea"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "social_links",
        sa.Column("social_network", sa.String(length=55), nullable=False),
        sa.Column("link", sa.String(length=255), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_social_links_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_social_links")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("social_links")
    # ### end Alembic commands ###
