import pymysql

server = pymysql.connect(host="localhost", user="root", passwd="")
cursor = server.cursor()
sql = "CREATE DATABASE IF NOT EXISTS kursai_su_python;"
cursor.execute(sql)


