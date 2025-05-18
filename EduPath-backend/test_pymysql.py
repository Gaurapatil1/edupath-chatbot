import pymysql

print("Starting PyMySQL connection test...")

try:
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='@Gauravpatil123',  # Replace with your MySQL password
        database='edupath_db',
        connect_timeout=5
    )
    print("Connected successfully using PyMySQL!")
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        print("MySQL version:", version[0])

except pymysql.MySQLError as e:
    print("Connection failed:", e)

finally:
    try:
        connection.close()
        print("Connection closed.")
    except:
        print("Connection was not established.")