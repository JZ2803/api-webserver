from init import db, ma
from datetime import date
from marshmallow import fields
from sqlalchemy import Date, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Define the Comment model
class Comment(db.Model):
    __tablename__ = 'comments'  # Set the table name to 'comments'

    id: Mapped[int] = mapped_column(primary_key=True)  # Define the id attribute as a primary key integer
    text: Mapped[str] = mapped_column(Text())  # Define the text attribute as a text type
    date_created: Mapped[date]  # Define the date_created attribute as a date

    enrolment_id: Mapped[int] = mapped_column(ForeignKey('enrolments.id'))  # Define the enrolment_id attribute as a foreign key to 'enrolments' table
    enrolment: Mapped['Enrolment'] = relationship(back_populates='comments')  # Define the relationship with the 'enrolments' table
  
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))  # Define the user_id attribute as a foreign key to 'users' table
    user: Mapped['User'] = relationship(back_populates='comments')  # Define the relationship with the 'users' table

# Define the Comment schema
class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['email'])  # Define the nested schema for 'user' attribute to include only 'email'
 
    class Meta:
        fields = ('id', 'date_created', 'text','enrolment_id', 'user_id', 'user') # Define the fields to include in the schema