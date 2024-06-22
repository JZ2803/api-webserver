from init import db, ma
from marshmallow import fields
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Comment(db.Model):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text())

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='comments')

    enrolment_id: Mapped[int] = mapped_column(ForeignKey('enrolments.id'))
    enrolment: Mapped['Enrolment'] = relationship(back_populates='comments')

class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'text', 'user_id', 'enrolment_id')