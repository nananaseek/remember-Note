import os

from tortoise import Tortoise


async def startup_db():
    await Tortoise.init(
        db_url=f"postgres://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}",
        modules={
            'models': [
                'database.model',
            ]
        }
    )

    await Tortoise.generate_schemas()


async def shutdown_db():
    await Tortoise.close_connections()
