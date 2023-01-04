from sqlalchemy.orm import Session

from . import models, schemas
from . import hashing


# SqlAlchemy ORM query to get all users.
def get_users(db: Session):
    return db.query(models.User).all()


# SqlAlchemy ORM query to create a new user.
def create_user(db: Session, user: schemas.UserSchema):
    db_user = models.User(name=user.name,dob = user.dob,email = user.email,password = hashing.get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# SqlAlchemy ORM query to update any existing user.
def update_user(db: Session, user_id: str, user: schemas.UserSchema):
    db.query(models.User).filter(models.User.id == user_id).update({models.User.name:user.name,models.User.dob : user.dob,models.User.password : hashing.get_password_hash(user.password)}, synchronize_session = False)
    db.commit()
    return {"msg":"credentials updated"}

# SqlAlchemy ORM query to delete any user.
def del_user(db: Session,user_id:str):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return {"msg":"User deleted successfully"}

