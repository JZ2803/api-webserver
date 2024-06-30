from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Define the ActivityType model
class ActivityType(db.Model):
    __tablename__ = 'activity_types'  # Set the table name to 'activity_types'


    id: Mapped[int] = mapped_column(primary_key=True)  # Define the id attribute as a primary key integer
    name: Mapped[str] = mapped_column(String()) # Define the name attribute as a string

    activities: Mapped[List['Activity']] = relationship(back_populates='activity_type')  # Define the relationship with the 'activities' table


# Define the ActivityType schema
class ActivityTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')  # Define the fields to include in the schema as ('id', 'name')