import pymysql

def connect_to_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='healthcare_bot_db',
        cursorclass=pymysql.cursors.DictCursor  # Ensures results are returned as dictionaries
    )
    return connection
