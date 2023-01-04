from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from .database import Base
import uuid



def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"
    id = Column(String, name="uuid", primary_key=True, default=generate_uuid)
    name = Column(String)
    dob = Column(Date)
    email = Column(String, unique=True,index=True)
    password = Column(String)