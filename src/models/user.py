from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow.validate import And, Length, Regexp

# Define User model
class User(db.Model):
    __tablename__ = 'users'  # Set the table name to 'users'


    id: Mapped[int] = mapped_column(primary_key=True)  # Define the id attribute as a primary key integer
    email: Mapped[str] = mapped_column(Text(), unique=True)  # Define the email attribute as a text type with a unique constraint
    password: Mapped[str] = mapped_column(String())  # Define the password attribute as a string
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')  # Define the is_admin attribute as a boolean with a server default of 'false'

    comments: Mapped[List['Comment']] = relationship(back_populates='user', cascade='all, delete')  # Define the relationship with the 'comments' table
    activities: Mapped[List['Activity']] = relationship(back_populates='user', cascade='all, delete')  # Define the relationship with the 'activities' table


# Define User Schemas
class UserSchema(ma.Schema):
    email = fields.Email(required=True)  # Define the email attribute as a required email field
    password = fields.String(required=True, validate=And(
        Length(min=8, error="Password must be at least 8 characters long"),
        Regexp('^(?=.*[a-zA-Z\d].*)[a-zA-Z\d!@#$%&*]{7,}$',
            error="Password must contain at least one uppercase letter, one lowercase letter, one digit and one special character"),
    ))  # Define the password attribute as a required and must contain at least one uppercase letter, one lowercase letter, one digit and one special character

    class Meta:
        fields = ('id', 'email', 'password', 'is_admin')  # Define the fields to include in the schema

class UserSummarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'is_admin')  # Define the fields to include in the summary schema