"""empty message

Revision ID: a5cfe890710d
Revises: 7352c721e0a4
Create Date: 2023-05-28 16:47:42.177222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5cfe890710d'
down_revision = '7352c721e0a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.drop_column('url_small')
        batch_op.drop_column('url_full')
        batch_op.drop_column('url_regular')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url_regular', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('url_full', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('url_small', sa.VARCHAR(length=500), autoincrement=False, nullable=True))

    # ### end Alembic commands ###