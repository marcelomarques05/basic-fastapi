"""Add Content Column

Revision ID: b11cc0bae5d8
Revises: 03674853ad01
Create Date: 2023-01-31 13:14:26.403478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b11cc0bae5d8'
down_revision = '03674853ad01'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
  pass


def downgrade() -> None:
  op.drop_column("posts", "content")
  pass
