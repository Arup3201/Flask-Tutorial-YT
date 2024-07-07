from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    password = Column(String(200), nullable=False)