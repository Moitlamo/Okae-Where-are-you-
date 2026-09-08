# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Fetch the URL securely from GitHub Secrets or your .env file
# If it can't find the cloud URL, it defaults to sqlite for absolute safety, 
# but you want it hitting your PostgreSQL string.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///okae_app.db")

# PostgreSQL engines don't need the 'check_same_thread' argument that SQLite does
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    # Fix for some PaaS environments that provide 'postgres://' instead of 'postgresql://'
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
