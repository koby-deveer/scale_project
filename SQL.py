# Importing module
import mysql.connector

# Creating connection object

def SQL(data):
	mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "valcoscale12345@",
	database="VALCO_RECORDS"
	)

	# Printing the connection object
	print(mydb)
	cursor=mydb.cursor()
	dbFunc="INSERT INTO RECORD VALUES(%s,%s,%s,%s)"
	cursor.execute(dbFunc,data)
	mydb.commit()
	
	mydb.close()
