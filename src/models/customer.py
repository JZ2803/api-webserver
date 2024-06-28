from init import db, ma
from marshmallow import fields
from typing import List
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Customer(db.Model):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String())
    last_name: Mapped[str] = mapped_column(String())
    email: Mapped[str] = mapped_column(Text())
    phone_no: Mapped[str] = mapped_column(String(10))

    plants: Mapped[List['Plant']] = relationship(back_populates='customer', cascade='all, delete')

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_no')

class CustomerPlantSchema(ma.Schema):
    plants = fields.Nested('PlantEnrolmentSchema', many=True, exclude=['customer_id'])

    class Meta:
        fields = ('first_name', 'last_name', 'plants')