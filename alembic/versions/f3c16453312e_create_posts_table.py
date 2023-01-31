"""Create Posts Table

Revision ID: f3c16453312e
Revises: 
Create Date: 2023-01-31 13:06:00.234558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3c16453312e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
  sa.Column("title", sa.String(), nullable=False))
  pass



def downgrade():
  op.drop_table("posts")
  pass