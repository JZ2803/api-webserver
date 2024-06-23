from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Plant(db.Model):
    __tablename__ = 'plants'

    id: Mapped[int] = mapped_column(primary_key=True)

    species_id: Mapped[int] = mapped_column(ForeignKey('species.id'))
    species: Mapped['Species'] = relationship(back_populates='plants') # Note: the word 'species' is both singular and plural

    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    customer: Mapped['Customer'] = relationship(back_populates='plants')

    enrolments: Mapped[List['Enrolment']] = relationship(back_populates='plant')

class PlantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'species_id', 'customer_id')