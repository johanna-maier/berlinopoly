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


def reset_database():
    """Drops and recreates the PostgreSQL database."""
    try:
        # Connect to the default PostgreSQL database
        conn = psycopg2.connect(dbname='postgres', user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        # Drop the database if it exists
        cur.execute(f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '{DB_NAME}';")
        cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
        print(f"Database {DB_NAME} dropped successfully.")

        # Create the database
        cur.execute(f"CREATE DATABASE {DB_NAME};")
        print(f"Database {DB_NAME} created successfully.")

        # Close connections
        cur.close()
        conn.close()

        # Connect to the new database to grant privileges
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        cur = conn.cursor()

        # Grant permissions
        cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};")
        print(f"Granted all privileges on {DB_NAME} to {DB_USER}.")

        # Close connections
        cur.close()
        conn.close()
        print("Database reset completed successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    reset_database()