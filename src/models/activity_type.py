from init import db, ma
from typing import List
from marshmallow import fields
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ActivityType(db.Model):
    __tablename__ = 'activity_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())

    activities: Mapped[List['Activity']] = relationship(back_populates='activity_type', cascade='all, delete')

class ActivityTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')