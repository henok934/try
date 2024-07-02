from sqlalchemy import *
from models.base import Base,BaseModel
from sqlalchemy.orm import relationship
from hashlib import md5
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel, Base, UserMixin):
    password_length = (0, None)
    password_regex = None
    __tablename__ = 'users'
    fname = Column(String(20),nullable = False)
    lname = Column(String(20),nullable = False)
    username = Column(String(20),nullable = False,unique = True)
    password = Column(String(10),nullable = False)
    gender = Column(String(5),nullable = False)
    phone = Column(Integer,nullable = False)
    email = Column(String(30),nullable = False, unique = True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
