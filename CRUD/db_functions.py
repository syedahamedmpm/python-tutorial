import mysql.connector
from mysql.connector import Error
from db_config import get_db_connection


def get_customers():
    try:
        conn = get_db_connection()
        print('conn',conn)
        cursor = conn.cursor()
        print('cursor',cursor)
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        print('rows',rows)
        return rows

    except Error as e:
        print("DB Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
