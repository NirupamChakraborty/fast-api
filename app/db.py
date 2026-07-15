from collections.abc import AsyncGenerator
import uuid

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.postgresql import UUID


DATABASE_URL = "sqlite+aiosqlite:///./test.db"