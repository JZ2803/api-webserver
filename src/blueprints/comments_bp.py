from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.enrolment import Enrolment
from models.comment import Comment, CommentSchema

# Define a Blueprint for comments
comments_bp = Blueprint('comments', __name__, url_prefix="/comments")

# Define a route for creating a new comment
@comments_bp.route("/<int:enrolment_id>", methods=['POST'])
@jwt_required() # Require JWT authentication for this route
def create_comment(enrolment_id):
    db.get_or_404(Enrolment, enrolment_id)  # Get the enrolment from the database using its ID
    comment_info = CommentSchema(only=['text', 'date_created']).load(request.json, unknown='exclude')  # Load the comment information from the request JSON using the CommentSchema
    comment = Comment(
        text=comment_info['text'],
        date_created=comment_info['date_created'],
        enrolment_id=enrolment_id,
        user_id=get_jwt_identity()
    )  # Create a new Comment object with the provided information and the current user's ID
    db.session.add(comment)  # Add the new comment to the database session
    db.session.commit()  # Commit the changes to the database
    return CommentSchema(exclude=['user_id]']).dump(comment), 201  # Return the newly created comment in JSON format and 201 status code

# Define a route for deleting a comment
@comments_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id # Require JWT authentication for this route and user must be an admin
def delete_activity(id):
    comment = db.get_or_404(Comment, id)  # Get the comment from the database using its ID or return 404 error
    db.session.delete(comment)  # Delete the comment from the database
    db.session.commit()  # Commit the changes to the database
    return {'message': "Deleted successfully"}  # Return an error message indicating that the comment has been deleted