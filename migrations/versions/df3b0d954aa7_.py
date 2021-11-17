"""empty message

Revision ID: df3b0d954aa7
Revises: aecbcf2b2fdb
Create Date: 2021-11-16 11:35:09.710557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df3b0d954aa7'
down_revision = 'aecbcf2b2fdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('starship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('starships_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['starships_id'], ['starships_details.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('starship')
    # ### end Alembic commands ###