from datetime import date
from typing import List
from init import db, ma
from marshmallow import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Define Enrolment model
class Enrolment(db.Model):
    __tablename__ = 'enrolments'  # Set the table name to 'enrolments'

    id: Mapped[int] = mapped_column(primary_key=True)  # Define the id attribute as a primary key integer
    start_date: Mapped[date]  # Define the start_date attribute as a date
    end_date: Mapped[date]  # Define the end_date attribute as a date

    plant_id: Mapped[int] = mapped_column(ForeignKey('plants.id'))  # Define the plant_id attribute as a foreign key to 'plants' table
    plant: Mapped['Plant'] = relationship(back_populates='enrolments')  # Define the relationship with the 'plants' table

    activities: Mapped[List['Activity']] = relationship(back_populates='enrolment', cascade='all, delete')  # Define the relationship with the 'activities' table

    comments: Mapped[List['Comment']] = relationship(back_populates='enrolment', cascade='all, delete')  # Define the relationship with the 'comments' table

# Define Enrolment schemas
class EnrolmentSchema(ma.Schema):
    activities = fields.Nested('ActivitySchema', many=True, exclude=['activity_type_id'])  # Define the nested schema for 'activities' attribute to exclude 'activity_type_id'
    comments = fields.Nested('CommentSchema', many=True, exclude=['enrolment_id'])  # Define the nested schema for 'comments' attribute to exclude 'enrolment_id'
    class Meta:
        fields = ('id', 'start_date', 'end_date', 'plant_id', 'activities', 'comments')  # Define the fields to include in the schema

class EnrolmentNewCustomerSchema(ma.Schema):
    plant = fields.Nested('PlantCustomerSchema', exclude=['specie_id'])  # Define the nested schema for 'plant' attribute to exclude 'specie_id'
    class Meta:
        fields = ('id', 'start_date', 'end_date', 'plant')  # Define the fields to include in the schema