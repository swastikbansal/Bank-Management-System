import mysql.connector

mysql_pswd=input("Enter your MySQL Login Password :")

try:
    mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    password=mysql_pswd,    
    database="banking")

    if mycon.is_connected():
        print("Connection Successfull!!")

    cur=mycon.cursor()
    mycon.autocommit=True

    cur.execute("DELETE FROM clients_data")
    print("Tables have been Reset Successfully!!")

except:
    print("\nUnable to connect!\nMaybe Password is wrong...")