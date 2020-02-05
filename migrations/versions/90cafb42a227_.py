"""empty message

Revision ID: 90cafb42a227
Revises: ee80350583db
Create Date: 2020-02-05 02:18:43.054692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90cafb42a227'
down_revision = 'ee80350583db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_group',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_group')
    op.drop_table('group')
    # ### end Alembic commands ###
