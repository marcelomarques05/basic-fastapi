"""User Table

Revision ID: 5d892e4df647
Revises: b11cc0bae5d8
Create Date: 2023-01-31 13:18:14.923504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d892e4df647'
down_revision = 'b11cc0bae5d8'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table('users',
  sa.Column('id', sa.Integer(), nullable=False),
  sa.Column('email', sa.Integer(), nullable=False),
  sa.Column('password', sa.Integer(), nullable=False),
  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
  sa.PrimaryKeyConstraint('id'),
  sa.UniqueConstraint('email')
  )

def downgrade():
  op.drop_table('users')
