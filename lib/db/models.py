# db/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    guests = relationship("Guest", back_populates="event", cascade="all, delete-orphan")
    expenses = relationship("Expense", back_populates="event", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Event(name={self.name}, date={self.date})>"

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'))

    event = relationship("Event", back_populates="guests")

    def __repr__(self):
        return f"<Guest(name={self.name}, email={self.email})>"

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'))

    event = relationship("Event", back_populates="expenses")

    def __repr__(self):
        return f"<Expense(name={self.name}, amount={self.amount})>"
