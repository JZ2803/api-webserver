from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow.validate import And, Length, Regexp

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(Text())
    password: Mapped[str] = mapped_column(String())
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

    comments: Mapped[List['Comment']] = relationship(back_populates='user', cascade='all, delete')
    activities: Mapped[List['Activity']] = relationship(back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=And(
        Length(min=8, error="Password must be at least 8 characters long"),
        Regexp('^(?=.*[a-zA-Z\d].*)[a-zA-Z\d!@#$%&*]{7,}$',
            error="Password must contain at least one uppercase letter, one lowercase letter, one digit and one special character"),
    ))

    class Meta:
        fields = ('id', 'email', 'password', 'is_admin')

class UserSummarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'is_admin')