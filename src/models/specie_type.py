from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class SpecieType(db.Model):
    __tablename__ = 'specie_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())

    species: Mapped[List['Specie']] = relationship(back_populates='specie_type')

class SpecieTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')