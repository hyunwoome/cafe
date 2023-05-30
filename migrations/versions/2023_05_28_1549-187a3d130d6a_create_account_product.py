"""create account, product

Revision ID: 187a3d130d6a
Revises: 
Create Date: 2023-05-28 15:49:30.605513

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '187a3d130d6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('phone', sa.String(20), nullable=False),
        sa.Column('password', sa.String(100), nullable=False),
        sa.Column('is_superuser', sa.Boolean(), nullable=True),
        sa.Column('create_date', sa.DateTime(), nullable=False),
        sa.Column('update_date', sa.DateTime(), nullable=True),
        sa.Column('delete_date', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.Column("category", sa.String(10), nullable=False),
        sa.Column("size", sa.String(10), nullable=False),
        sa.Column("name", sa.String(30), nullable=False),
        sa.Column("tag", sa.Text(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("cost", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column('barcode', sa.String(50), nullable=False),
        sa.Column('expiration_date', sa.DateTime(), nullable=False),
        sa.Column('create_date', sa.DateTime(), nullable=False),
        sa.Column('update_date', sa.DateTime(), nullable=True),
        sa.Column('delete_date', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["account_id"], ["account.id"], ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "invalid_token",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(300), nullable=False),
        sa.Column('create_date', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    pass
