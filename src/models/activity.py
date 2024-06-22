from datetime import date
from init import db, ma
from marshmallow import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Activity(db.Model):
    __tablename__ = 'activities'

    id: Mapped[int] = mapped_column(primary_key=True)
    date_performed: Mapped[date]

    activity_type_id: Mapped[int] = mapped_column(ForeignKey('activity_types.id'))
    activity_type: Mapped['ActivityType'] = relationship(back_populates='activities')

    enrolment_id: Mapped[int] = mapped_column(ForeignKey('enrolments.id'))
    enrolment: Mapped['Enrolment'] = relationship(back_populates='activities')

class ActivitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_performed', 'activity_type_id', 'enrolment_id')
