from init import db, ma
from datetime import date
from marshmallow import fields
from sqlalchemy import Date, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Comment(db.Model):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text())
    date_created: Mapped[date]

    enrolment_id: Mapped[int] = mapped_column(ForeignKey('enrolments.id'))
    enrolment: Mapped['Enrolment'] = relationship(back_populates='comments')

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='comments')

class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['email'])
    
    class Meta:
        fields = ('id', 'date_created', 'text','enrolment_id', 'user')