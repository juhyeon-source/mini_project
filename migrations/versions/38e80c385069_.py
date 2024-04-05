"""empty message

Revision ID: 38e80c385069
Revises: 998953ba4265
Create Date: 2024-04-05 10:54:01.702435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38e80c385069'
down_revision = '998953ba4265'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DATETIME(), nullable=True))

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DATETIME(), nullable=True))

    # ### end Alembic commands ###
