"""empty message

Revision ID: 638027b3e40a
Revises: 3bfea26489e5
Create Date: 2021-11-26 16:29:29.027181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '638027b3e40a'
down_revision = '3bfea26489e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favouritespeople',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'people_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favouritespeople')
    # ### end Alembic commands ###
