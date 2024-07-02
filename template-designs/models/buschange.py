from models.base import Base
from models.base import BaseModel
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import ForeignKey
class Buschange(BaseModel, Base):
    __tablename__ = 'buschanges'
    date = Column(String(30), nullable = False)
    depcity = Column(String(20), nullable = False)
    descity = Column(String(20), nullable = False)
    side_no = Column(Integer, nullable = False)
    plate_no = Column(Integer, nullable = False)
    new_plate_no = Column(Integer, nullable = False)
    new_side_no = Column(Integer, nullable = False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
