from init import db
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required

def admin_only(fn):
    @jwt_required()
    def inner():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        user = db.session.scalar(stmt)
        if user:
            return fn()
        return {'error': "You must be an admin to access this resource"}, 403
    
    return inner


def admin_only2(fn):
    @jwt_required()
    def inner2(id):
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        user = db.session.scalar(stmt)
        if user:
            return fn(id)
        return {'error': "You must be an admin to access this resource"}, 403
    
    return inner2