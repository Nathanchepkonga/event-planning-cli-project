from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    
    guests = relationship('Guest', back_populates='event')
    expenses = relationship('Expense', back_populates='event')

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    event_id = Column(Integer, ForeignKey('events.id'))
    
    event = relationship('Event', back_populates='guests')

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Float)
    event_id = Column(Integer, ForeignKey('events.id'))
    
    event = relationship('Event', back_populates='expenses')

# Setup the SQLite database connection
engine = create_engine('sqlite:///event_planning.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
