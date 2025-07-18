"""Add annotations to tables

Revision ID: e4fc04d1a442
Revises: b77ca9d2de7e
Create Date: 2025-06-27 21:45:35.099713

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'e4fc04d1a442'
down_revision: Union[str, Sequence[str], None] = 'b77ca9d2de7e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Applies the migration to add the 'annotations' column.

    This function adds a new column named 'annotations' of type JSON to the 'tool'
    table. It includes a server-side default of an empty JSON object ('{}') to ensure
    that existing rows get a non-null default value.
    """
    op.add_column('tools', sa.Column('annotations', sa.JSON(), server_default=sa.text("'{}'"), nullable=False))


def downgrade() -> None:
    """
    Reverts the migration by removing the 'annotations' column.

    This function provides a way to undo the migration, safely removing the
    'annotations' column from the 'tool' table.
    """
    op.drop_column('tools', 'annotations')
