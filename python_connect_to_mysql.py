import mysql.connector
connection = mysql.connector.connect(host='localhost',username='root',password='R@dhavallabh108',database='database1')
my_cursor=connection.cursor()
connection.commit()
connection.close()
print(" connection successful")