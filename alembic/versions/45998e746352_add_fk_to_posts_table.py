"""Add FK to Posts Table

Revision ID: 45998e746352
Revises: 5d892e4df647
Create Date: 2023-01-31 13:25:35.543513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45998e746352'
down_revision = '5d892e4df647'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
  op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
  op.drop_constraint("posts_usets_fk", table_name="posts")
  op.drop_column("posts", "owner_id")
  