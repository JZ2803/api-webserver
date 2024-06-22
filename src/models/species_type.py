from init import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class SpeciesType(db.Model):
    __tablename__ = 'species_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())

    species: Mapped['Species'] = relationship(back_populates='species_types')