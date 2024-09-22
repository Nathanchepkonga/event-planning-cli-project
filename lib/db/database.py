# db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database
DATABASE_URL = "sqlite:///events.db"

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Base class for models
Base = declarative_base()

def init_db():
    import lib.db.models  # Import models to register them with Base
    Base.metadata.create_all(bind=engine)
