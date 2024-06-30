from init import db, ma
from marshmallow import fields
from typing import List
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Define the Customer model
class Customer(db.Model):
    __tablename__ = 'customers'  # Set the table name to 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)   # Define the id attribute as a primary key integer
    first_name: Mapped[str] = mapped_column(String())  # Define the first_name attribute as a string
    last_name: Mapped[str] = mapped_column(String())  # Define the last_name attribute as a string
    email: Mapped[str] = mapped_column(Text())  # Define the email attribute as a text type
    phone_no: Mapped[str] = mapped_column(String(10))  # Define the phone_no attribute as a string with a maximum length of 10

    plants: Mapped[List['Plant']] = relationship(back_populates='customer', cascade='all, delete')  # Define the relationship with the 'plants' table

# Define the Customer schema
class CustomerSchema(ma.Schema):
    plants = fields.Nested('PlantEnrolmentSchema', many=True, exclude=['customer_id'])  # Define the nested schema for 'plants' attribute to exclude 'customer_id'
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_no', 'plants')  # Define the fields to include in the schema