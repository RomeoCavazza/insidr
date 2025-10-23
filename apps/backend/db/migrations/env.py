import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# --- ajout: importe ta metadata ---
from db.base import Base, DATABASE_URL

# this is the Alembic Config object
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# target_metadata from your models
target_metadata = Base.metadata

def run_migrations_offline():
    url = os.getenv("DATABASE_URL", DATABASE_URL)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    configuration = config.get_section(config.config_ini_section) or {}
    configuration["sqlalchemy.url"] = os.getenv("DATABASE_URL", DATABASE_URL)

    connectable = engine_from_config(
        configuration, prefix="sqlalchemy.", poolclass=pool.NullPool
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()