from logging.config import fileConfig
import asyncio
from alembic import context
from backend.core.db.models import Base
from sqlalchemy import engine_from_config, pool
from config import settings

from sqlalchemy.ext.asyncio import async_engine_from_config
from backend.models.tables.category import Category
from backend.models.tables.user import User
from backend.models.tables.user_response import UserResponse
from backend.models.tables.feedback import Feedback
from backend.models.tables.question import Question


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

#
# local_db_url = settings.async_db_url.replace("@db:", "@localhost:")
# config.set_main_option("sqlalchemy.url", local_db_url)
#

config.set_main_option("sqlalchemy.url", settings.async_db_url)




target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()