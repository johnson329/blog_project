"""empty message

Revision ID: 2226f430702a
Revises: bbdb2163fc87
Create Date: 2020-02-05 20:41:14.992114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2226f430702a'
down_revision = 'bbdb2163fc87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_group_ibfk_1', 'user_group', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('user_group_ibfk_1', 'user_group', 'group', ['group_id'], ['id'])
    # ### end Alembic commands ###
