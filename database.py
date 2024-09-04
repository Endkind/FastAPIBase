from typing import Type
from sqlalchemy import create_engine, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DatabaseConfig

DATABASE_URL = DatabaseConfig.URL

engine = create_engine(DATABASE_URL)
dialect = engine.url.get_dialect().name
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def _get_id_type(dialect_name) -> Type[Integer] | Type[BigInteger]:
    if dialect_name == 'sqlite':
        return Integer
    elif dialect_name == 'postgresql':
        return BigInteger
    else:
        raise NotImplementedError(f"dialect {dialect_name} not implemented")


def get_id_type_for_dialect() -> Type[Integer] | Type[BigInteger]:
    return _get_id_type(dialect)
