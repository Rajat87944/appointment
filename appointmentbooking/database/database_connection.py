import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rajat@123",
        database="appointment"
    )

def fetch_data(query, params=None):
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    mycursor.execute(query, params or ())
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return myresult
