# init_db.py
from database import engine, Base
import models 

def initialize_database():
    print("Connecting to Supabase...")
    # This creates the tables in your live cloud database
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully in Supabase!")

if __name__ == "__main__":
    initialize_database()
