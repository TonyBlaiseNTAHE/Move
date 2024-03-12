#!/usr/bin/python3


"""
user module
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from movie import Movie
from subscription import Subscription
from paypal import Payment
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    subscriptions = relationship('Subscription', back_populates='user')
    payments = relationship('Payment', back_populates='user')
    
    def __repr__(self):
        return f'<User {self.username}>'