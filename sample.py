import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

def convertToBinaryData(filename):
	#Convert digital data to binary format
	with open(filename, 'rb') as file:
		binaryData = file.read()
	return binaryData

def insertBLOB(photo):
	print("Inserting BLOB into database table")
	try:
		connection = mysql.connector.connect(host='localhost',                     database='python_db'connection = mysql.connector.connect(host='localhost',
                             database='smartlab',
                             user='root',
                             password='18mcpc13')
		cursor = connection.cursor(prepared=True)
		sql_insert_blob_query = """ INSERT INTO `visitors`
                          (`timestamp`, `photo`) VALUES (%s,%s)"""
	bin_photo = convertToBinaryData(photo)
	timestamp = str(datetime.now())

	insert_blob_tuple = (timestamp,bin_photo)
	result  = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
	connection.commit()
	print ("record inserted into database table", result)
	except mysql.connector.Error as error :
		connection.rollback()
		print("Failed inserting BLOB data into MySQL table {}".format(error))
	finally:
		#closing database connection.
		if(connection.is_connected()):
			cursor.close()
			connection.close()
			print("MySQL connection is closed")

insertBLOB("/tmp/picture.jpg")
