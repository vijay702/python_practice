import json
import mysql.connector

data = open('C:\\Users\\user\\Downloads\\zipcodes_coordinates123.json')
json_data = json.load(data)
print(json_data)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="k12_find_my_neighbour"
)
count =0
for x in  json_data:
    print(x)
    mycursor = mydb.cursor()
    json_data1 = json_data[x]
    json_data1_string = str(json_data1)
    json_data_final_value = json_data1_string.replace("'", '"')
    sql = f"update k12_find_my_neighbour.zip_code_table set border_data ='{json_data_final_value}'  where zip ={x} "

    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    count +=1
    print(count)