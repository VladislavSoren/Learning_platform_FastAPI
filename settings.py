"""File with settings and configs for the project"""

from envparse import Env

env = Env()

postgres_port = 6543

'''
Чтобы асинхронно использовать sqlalchemy, обязательно нужно указать "postgresql+asyncpg"
'''
REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default=f"postgresql+asyncpg://postgres:postgres@0.0.0.0:{postgres_port}/postgres"
)  # connect string for the database
