# This file previously contained the SQLAlchemy User model.
# SQLAlchemy models are no longer used directly.
# If you need data validation or a structured representation for user data,
# consider using Pydantic models.
# 
# Example Pydantic model (optional):
# from pydantic import BaseModel, EmailStr
# 
# class UserBase(BaseModel):
#     email: EmailStr
# 
# class UserCreate(UserBase):
#     password: str
# 
# class UserInDB(UserBase):
#     id: int
#     is_active: bool
# 
#     class Config:
#         orm_mode = True # or from_attributes = True for Pydantic v2