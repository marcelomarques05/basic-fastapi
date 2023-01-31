"""Add Phone Number

Revision ID: 21181e9a8fdf
Revises: a050c6bc289b
Create Date: 2023-01-31 13:40:16.376182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21181e9a8fdf'
down_revision = 'a050c6bc289b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
