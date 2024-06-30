from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Define Specie model
class Specie(db.Model):
    __tablename__ = 'species'  # Set the table name to 'species'

    id: Mapped[int] = mapped_column(primary_key=True)  # Define the id attribute as a primary key integer
    name: Mapped[str] = mapped_column(String())  # Define the name attribute as a string
    
    specie_type_id: Mapped[int] = mapped_column(ForeignKey('specie_types.id'))  # Define the specie_type_id attribute as a foreign key to 'specie_types' table
    specie_type: Mapped['SpecieType'] = relationship(back_populates='species')  # Define the relationship with the 'specie_types' table

    plants: Mapped[List['Plant']] = relationship(back_populates='specie')  # Define the relationship with the 'plants' table

# Define Specie schema
class SpecieSchema(ma.Schema):
    specie_type = fields.Nested('SpecieTypeSchema', only=['name'])  # Define the nested schema for 'specie_type' attribute to include only 'name'

    class Meta:
        fields = ('id', 'name', 'specie_type') # Define the fields to include in the schema