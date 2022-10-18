"""followers

Revision ID: 129fe2da4317
Revises: de1524d8eb80
Create Date: 2022-10-18 11:31:51.418578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '129fe2da4317'
down_revision = 'de1524d8eb80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
