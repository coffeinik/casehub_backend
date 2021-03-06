"""first migration

Revision ID: 67665cec7ec8
Revises: 145230d3147d
Create Date: 2021-01-11 01:57:00.119660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67665cec7ec8'
down_revision = '145230d3147d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('steps', 'case_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('steps', 'case_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
