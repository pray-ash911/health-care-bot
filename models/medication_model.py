from config.db_config import connect_to_db

def fetch_medication_by_id(medicine_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM medications WHERE id = %s", (medicine_id,))
    medication = cursor.fetchone()
    connection.close()
    return medication

def insert_medication(medication_info):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO medications (Username, name, dose, frequency, time) "
        "VALUES (%s, %s, %s, %s, %s)",
        (medication_info['Username'], medication_info['name'], medication_info['dose'],
         medication_info['frequency'], medication_info['time'])
    )
    connection.commit()
    connection.close()

def update_medication(medicine_id, medication_info):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE medications SET Username=%s, name=%s, dose=%s, frequency=%s, time=%s WHERE id=%s",
        (medication_info['Username'], medication_info['name'], medication_info['dose'],
         medication_info['frequency'], medication_info['time'], medicine_id)
    )
    connection.commit()
    connection.close()
