#用sqlite3读取数据
import sqlite3
con=sqlite3.connect("iris.db")

cursor=con.execute("SELECT * FROM iris WHERE Species = 'virginica'")
for row in cursor:
	print(rwo[0],rwo[1],rwo[2],rwo[3],rwo[4])