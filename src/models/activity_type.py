from init import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

class ActivityType(db.Model):
    __tablename__ = 'activity_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())

    activities: Mapped['Activity'] = relationship(back_populates='activity_type')
    