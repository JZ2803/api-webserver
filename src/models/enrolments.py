from datetime import date
from init import db, ma
from marshmallow import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Enrolment(db.Model):
    __tablename__ = 'enrolments'

    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[date]
    end_date: Mapped[date]

    plant_id: Mapped[int] = mapped_column(ForeignKey('plants.id'))
    plant: Mapped['Plant'] = relationship(back_populates='enrolments')

class EnrolmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_date', 'end_date', 'plant_id')