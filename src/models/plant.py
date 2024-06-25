from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Plant(db.Model):
    __tablename__ = 'plants'

    id: Mapped[int] = mapped_column(primary_key=True)

    specie_id: Mapped[int] = mapped_column(ForeignKey('species.id'))
    specie: Mapped['Specie'] = relationship(back_populates='plants')

    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    customer: Mapped['Customer'] = relationship(back_populates='plants')

    enrolments: Mapped[List['Enrolment']] = relationship(back_populates='plant', cascade='all, delete')

class PlantSchema(ma.Schema):
    specie = fields.Nested('SpecieSchema', only=['name'])
    class Meta:
        ordered = True
        fields = ('id', 'specie', 'customer_id')

class PlantEnrolmentSchema(ma.Schema):
    enrolments = fields.Nested('EnrolmentSchema', many=True)
    specie = fields.Nested('SpecieSchema', only=['name', 'specie_type'])
    class Meta:
        ordered = True
        fields = ('specie', 'customer_id', 'enrolments')