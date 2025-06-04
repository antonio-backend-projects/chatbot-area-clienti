
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', ''),
                database=os.getenv('DB_NAME', 'customer_db')
            )
        return cls._instance

    def get_cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

def db_query(query, params=None):
    db = Database()
    cursor = db.get_cursor()
    try:
        cursor.execute(query, params or ())
        if query.strip().lower().startswith('select'):
            return cursor.fetchall()
        db.commit()
        return True
    except Exception as e:
        print(f"Database error: {e}")
        return False
