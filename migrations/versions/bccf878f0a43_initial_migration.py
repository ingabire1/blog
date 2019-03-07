"""Initial Migration

Revision ID: bccf878f0a43
Revises: 
Create Date: 2019-03-06 17:18:10.118238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bccf878f0a43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('full_time', sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
