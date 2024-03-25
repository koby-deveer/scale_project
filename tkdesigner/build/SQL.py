# Importing module
import mysql.connector
import logging

#Creating and setting logger paramas
LoggerSQL=logging.getLogger('SQL ERROR LOGGER')
handler=logging.FileHandler('SQLFile.log')
format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setLevel(logging.ERROR)
handler.setFormatter(format)
LoggerSQL.addHandler(handler)

# Creating connection object
def SQL_IN(data):
	try:
		mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "valcoscale12345@",
		database="VALCO_RECORDS"
		)

		# Printing the connection object
		print(mydb)
		cursor=mydb.cursor()
		dbFunc="INSERT INTO WEIGHIN VALUES(%s,%s,%s,%s,%s,%s,%s)"
		cursor.execute(dbFunc,data)
		mydb.commit()
		
		mydb.close()
	except mysql.connector.Error as Error:
		LoggerSQL.error("Error Occured",exc_info=True)



def SQL_OUT(data):
	try:
		mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "valcoscale12345@",
		database="VALCO_RECORDS"
		)

		print(mydb)
		cursor=mydb.cursor()
		dbFunc="INSERT INTO WEIGHOUT VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		cursor.execute(dbFunc,data)
		mydb.commit()
		mydb.close()
	except mysql.connector.Error as Error:
		LoggerSQL.error("Error Occured",exc_info=True)
