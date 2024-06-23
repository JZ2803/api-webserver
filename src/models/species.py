from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Species(db.Model):
    __tablename__ = 'species'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    
    species_type_id: Mapped[int] = mapped_column(ForeignKey('species_types.id'))
    species_type: Mapped['SpeciesType'] = relationship(back_populates='species')

    plants: Mapped[List['Plant']] = relationship(back_populates='species')

class SpeciesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'species_type_id')