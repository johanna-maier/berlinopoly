import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Load environment variables
load_dotenv()

# Read values from .env file
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


def setup_database():
    """Creates the PostgreSQL database and user if they don't exist."""
    try:
        # Connect to the default PostgreSQL database
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        # Check if the database already exists
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
        if not cur.fetchone():
            cur.execute(f"CREATE DATABASE {DB_NAME};")
            print(f"Database {DB_NAME} created successfully.")

        # Check if the user exists
        cur.execute(f"SELECT 1 FROM pg_roles WHERE rolname = '{DB_USER}';")
        if not cur.fetchone():
            cur.execute(f"CREATE USER {DB_USER} WITH PASSWORD '{DB_PASS}';")
            print(f"User {DB_USER} created successfully.")

        # Grant permissions
        cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};")
        print(f"Granted all privileges on {DB_NAME} to {DB_USER}.")

        # Close connections
        cur.close()
        conn.close()
        print("Database setup completed successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    setup_database()
