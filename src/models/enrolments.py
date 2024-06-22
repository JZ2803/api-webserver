from datetime import date
from init import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Enrolment(db.Model):
    __tablename__ = 'enrolments'

    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[date]
    end_date: Mapped[date]

    plant_id: Mapped[int] = mapped_column(ForeignKey('plants.id'))
    plant: Mapped['Plant'] = relationship(back_populates='enrolments')