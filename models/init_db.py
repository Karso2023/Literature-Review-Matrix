# https://stackoverflow.com/questions/8588126
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

conn = psycopg2.connect(database=DB_NAME, 
                        user=DB_USER,
                        password=DB_PASSWORD, 
                        host=DB_HOST, 
                        port=DB_PORT)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS review_matrix (
    id SERIAL PRIMARY KEY,
    data JSONB
);
""")
conn.commit()


cur.close()
conn.close()