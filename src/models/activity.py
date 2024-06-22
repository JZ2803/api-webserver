from datetime import date
from init import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Activity(db.Model):
    __tablename__ = 'activities'

    id: Mapped[int] = mapped_column(primary_key=True)
    date_performed: Mapped[date]

    activity_type_id: Mapped[int] = mapped_column(ForeignKey('activity_types.id'))
    activity_type: Mapped['ActivityType'] = relationship(back_populates='activities')

    enrolment_id: Mapped[int] = mapped_column(ForeignKey('enrolments.id'))
    enrolment: Mapped['Enrolment'] = relationship(back_populates='activities')
