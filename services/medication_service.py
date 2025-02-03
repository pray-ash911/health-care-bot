from models.medication_model import fetch_medication_by_id, insert_medication, update_medication
from config.db_config import connect_to_db

def get_all_medications():
    # Logic to get all medications from the database
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM medications")
    medications = cursor.fetchall()
    connection.close()
    return medications

def add_new_medication(medication_info):
    # Call model function to insert a new medication
    insert_medication(medication_info)

def update_medication_by_id(medicine_id, medication_info):
    # Call model function to update medication
    update_medication(medicine_id, medication_info)
