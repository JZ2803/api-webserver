from init import db, ma
from marshmallow import fields
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Species(db.Model):
    __tablename__ = 'species'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    
    type_id: Mapped[int] = mapped_column(ForeignKey('species_types.id'))
    type: Mapped['SpeciesType'] = relationship(back_populates='species')

class SpeciesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'type_id')