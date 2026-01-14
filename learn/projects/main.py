from dotenv import load_dotenv
import os

load_dotenv()

db_conn = os.getenv("DB_CONNECTION")

print(db_conn)
