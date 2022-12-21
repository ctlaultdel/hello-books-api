"""adds Book model to books table

Revision ID: 264d9ff4d56e
Revises: 46a87082814d
Create Date: 2022-12-20 17:26:23.820106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '264d9ff4d56e'
down_revision = '46a87082814d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('book')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='book_pkey')
    )
    op.drop_table('books')
    # ### end Alembic commands ###