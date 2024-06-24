import uuid
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.dialects.postgresql import UUID


class Base(DeclarativeBase):
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now)
    deleted_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = func.now()


class User(Base):
    __tablename__ = "records"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message: Mapped[TEXT] = mapped_column(TEXT)
