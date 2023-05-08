# importing module
from pandas import *
import mysql.connector

# read specific columns of csv file using Pandas
data = read_csv('C:\\Users\\user\\Downloads\\Georgia_lat_lan_final2.csv')
print(data)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="k12_find_my_neighbour"
)
for x in zip(data['INST_UID'], data['Latitude']):
    print(x)
    mycursor = mydb.cursor()
    sql = f"update k12_find_my_neighbour.school_data set lat ={x[1]}  where INST_UID ='{x[0]}' "

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")