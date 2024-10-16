# db_confiig.py (database snga connect grney kamm grxa yo function)
from dbm import error # yo dbm chai python ko database module ho to handle errors of database

import mysql.connector

def connect_to_db():
    """Connects to the MySQL database and returns the connection."""
    try:
        connection= mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="",
        database="medications_db"
)
        if connection.is_connected(): #is_connected is a method
            return connection

    except error as e: # yo error chai mathi from dbm import error bata ako ho

        print(f"Error is :{e}")
        return none