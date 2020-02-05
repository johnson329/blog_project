"""empty message

Revision ID: 67d0e5d07e0c
Revises: 90cafb42a227
Create Date: 2020-02-05 10:12:58.169461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67d0e5d07e0c'
down_revision = '90cafb42a227'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user_group', 'group', ['group_id'], ['id'])
    op.create_foreign_key(None, 'user_group', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_group', type_='foreignkey')
    op.drop_constraint(None, 'user_group', type_='foreignkey')
    # ### end Alembic commands ###
