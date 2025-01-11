import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError, SQLAlchemyError, ProgrammingError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("db_user_password.env")

# Retrieve database credentials from environment variables
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

# Define the database URL using the environment variables
db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

# Create the database engine
engine = create_engine(db_url)

def get_team_data(team1, team2):
    """
    Retrieve data for two specified teams from the database.
    """
    try:
        with engine.connect() as connection:
            # Query to select data for the specified teams
            query = text("SELECT * FROM data WHERE TEAM = :team1 OR TEAM = :team2")
            result = connection.execute(query, {"team1": team1, "team2": team2}).mappings().all()
            return result
    except (OperationalError, SQLAlchemyError, ProgrammingError) as e:
        print("An error occurred while interacting with the database.")
        print("Error:", e)
        return None
#print(get_team_data("ATL","BOS"))