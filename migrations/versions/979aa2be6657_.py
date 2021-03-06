"""empty message

Revision ID: 979aa2be6657
Revises: 29c89a5db17c
Create Date: 2020-02-08 03:55:13.835038

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '979aa2be6657'
down_revision = '29c89a5db17c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association',
    sa.Column('left_id', sa.Integer(), nullable=True),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['left_id'], ['left.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['right.id'], )
    )
    op.drop_table('middle')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('middle',
    sa.Column('left_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('right_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('left_id', 'right_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('association')
    # ### end Alembic commands ###
