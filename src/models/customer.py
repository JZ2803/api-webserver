from init import db, ma
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Customer(db.Model):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String())
    last_name: Mapped[str] = mapped_column(String())
    email: Mapped[str] = mapped_column(Text(320))

    plants: Mapped['Plant'] = relationship(back_populates='customer')

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email')