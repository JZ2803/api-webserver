from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.enrolment import Enrolment
from models.comment import Comment, CommentSchema

comments_bp = Blueprint('comments', __name__, url_prefix="/comments")

@comments_bp.route("/<int:id>", methods=['POST'])
@jwt_required()
def create_comment(id):
    """Creates a new comment for an existing enrolment in the database and returns such record."""
    db.get_or_404(Enrolment, id)
    comment_info = CommentSchema(only=['text', 'date_created']).load(request.json, unknown='exclude')
    comment = Comment(
        text=comment_info['text'],
        date_created=comment_info['date_created'],
        enrolment_id=id,
        user_id=get_jwt_identity()
    )
    db.session.add(comment)
    db.session.commit()
    return CommentSchema().dump(comment), 201

@comments_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_activity(id):
    """Deletes a comment from an enrolment in the database."""
    comment = db.get_or_404(Comment, id)
    db.session.delete(comment)
    db.session.commit()
    return {'message': "Deleted successfully"}