from core.config.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

dsn = (f"postgresql+asyncpg://{settings.pg.db_user}:{settings.pg.db_password}@"
       f"{settings.pg.db_host}:{settings.pg.db_port}/{settings.pg.db_name}")
engine = create_async_engine(dsn, echo=True, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore


async def get_session() -> AsyncSession:  # type: ignore
    async with async_session() as session:
        yield session
