import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="k12_find_my_neighbour"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM k12_find_my_neighbour.zip_code_table order by zip limit 41038;")
value = 400
myresult = mycursor.fetchall()

for x in myresult:
