"""Add Chef Table And Relations

Revision ID: 58d034403f1f
Revises: 2cd7df6efa57
Create Date: 2023-11-16 19:31:35.504800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58d034403f1f'
down_revision: Union[str, None] = '2cd7df6efa57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chefs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('recipes', sa.Column('chef_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'recipes', 'chefs', ['chef_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.drop_column('recipes', 'chef_id')
    op.drop_table('chefs')
    # ### end Alembic commands ###
