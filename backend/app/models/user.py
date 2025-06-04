# This file previously contained the SQLAlchemy User model.
# SQLAlchemy models are no longer used directly.
# If you need data validation or a structured representation for user data,
# consider using Pydantic models.

from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # Add other fields as necessary, e.g., full_name, etc.

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"