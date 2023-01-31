"""Add more columns

Revision ID: fb2eee38914a
Revises: 45998e746352
Create Date: 2023-01-31 13:29:59.588128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb2eee38914a'
down_revision = '45998e746352'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
  op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))


def downgrade():
  op.drop_column('posts', 'published')
  op.drop_column('posts', 'created_at')
