from datetime import date
from init import db, ma
from marshmallow import fields
from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Define the Activity model
class Activity(db.Model):
    __tablename__ = 'activities'  # Set the table name to 'activities'

    id: Mapped[int] = mapped_column(primary_key=True)  # Define the id attribute as a primary key integer
    date_performed: Mapped[date]  # Define the date_performed attribute as a date

    activity_type_id: Mapped[int] = mapped_column(ForeignKey('activity_types.id'))  # Define the activity_type_id attribute as a foreign key to 'activity_types' table
    activity_type: Mapped['ActivityType'] = relationship(back_populates='activities')  # Define the relationship with the 'activity_types' table

    enrolment_id: Mapped[int] = mapped_column(ForeignKey('enrolments.id'))  # Define the enrolment_id attribute as a foreign key to 'enrolments' table
    enrolment: Mapped['Enrolment'] = relationship(back_populates='activities')  # Define the relationship with the 'enrolments' table

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))  # Define the user_id attribute as a foreign key to 'users' table
    user: Mapped['User'] = relationship(back_populates='activities')  # Define the relationship with the 'users' table

# Define the Activity schema
class ActivitySchema(ma.Schema):
    """
    Define the ActivitySchema class that represents the schema for the 'activities' table.
    The class has a nested schema for 'activity_type' and 'user' attributes, and only includes specific fields.
    """
    activity_type = fields.Nested('ActivityTypeSchema', only=['name'])   # Define the nested schema for 'activity_type' attribute to include only 'name'
    user = fields.Nested('UserSchema', only=['email'])  # Define the nested schema for 'user' attribute to include only 'email'
    
    class Meta:
        fields = ('id', 'date_performed', 'activity_type_id', 'activity_type', 'user_id', 'user') # Define the fields to include in the schema