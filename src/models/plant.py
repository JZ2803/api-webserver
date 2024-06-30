from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Define Plant model
class Plant(db.Model):
    __tablename__ = 'plants'  # Set the table name to 'plants'

    id: Mapped[int] = mapped_column(primary_key=True)  # Define the id attribute as a primary key integer

    specie_id: Mapped[int] = mapped_column(ForeignKey('species.id'))  # Define the specie_id attribute as a foreign key to 'species' table
    specie: Mapped['Specie'] = relationship(back_populates='plants')  # Define the relationship with the 'species' table

    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))  # Define the customer_id attribute as a foreign key to 'customers' table
    customer: Mapped['Customer'] = relationship(back_populates='plants')  # Define the relationship with the 'customers' table

    enrolments: Mapped[List['Enrolment']] = relationship(back_populates='plant', cascade='all, delete')  # Define the relationship with the 'enrolments' table

# Define Plant Schemas
class PlantSchema(ma.Schema):
    specie = fields.Nested('SpecieSchema', only=['name', 'specie_type'])  # Define the nested schema for 'specie' attribute to include only 'name' and 'specie_type'
    enrolments = fields.Nested('EnrolmentSchema', many=True, exclude=['plant_id'])  # Define the nested schema for 'enrolments' attribute to exclude 'plant_id'
    class Meta:
        fields = ('id', 'specie_id', 'specie', 'customer_id', 'enrolments')  # Define the fields to include in the schema

class PlantCustomerSchema(ma.Schema):  # Used in EnrolmentNewCustomerSchema schema
    specie = fields.Nested('SpecieSchema', only=['name'])  # Define the nested schema for 'specie' attribute to include only 'name'
    customer = fields.Nested('CustomerSchema')  # Define the nested schema for 'customer' attribute
    class Meta:
        fields = ('id', 'specie_id', 'specie', 'customer')  # Define the fields to include in the schema