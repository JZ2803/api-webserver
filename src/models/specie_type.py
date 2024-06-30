from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Define SpecieType model
class SpecieType(db.Model):
    __tablename__ = 'specie_types'  # Set the table name to 'specie_types'

    id: Mapped[int] = mapped_column(primary_key=True)  # Define the id attribute as a primary key integer
    name: Mapped[str] = mapped_column(String())  # Define the name attribute as a string

    species: Mapped[List['Specie']] = relationship(back_populates='specie_type')  # Define the relationship with the 'species' table

# Define SpecieType schema
class SpecieTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')  # Define the fields to include in the schema