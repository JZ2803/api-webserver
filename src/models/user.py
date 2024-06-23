from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(Text())
    password: Mapped[str] = mapped_column(String())
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

    comments: Mapped[List['Comment']] = relationship(back_populates='user')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'is_admin')