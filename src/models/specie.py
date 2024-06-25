from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Specie(db.Model):
    __tablename__ = 'species'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    
    specie_type_id: Mapped[int] = mapped_column(ForeignKey('specie_types.id'))
    specie_type: Mapped['SpecieType'] = relationship(back_populates='species')

    plants: Mapped[List['Plant']] = relationship(back_populates='specie')

class SpecieSchema(ma.Schema):
    specie_type = fields.Nested('SpecieTypeSchema', only=['name'])
    
    class Meta:
        fields = ('id', 'name', 'specie_type')