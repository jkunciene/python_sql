import pymysql


class Datab():
    def __init__(self, databaseName, servername, username, password):
            self.n=databaseName
            db = pymysql.connect(host=servername, user=username, passwd=password)
            cursor = db.cursor()
            self.cursor = cursor
            cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(self.n))
            cursor.execute("use {};".format(self.n))

    def addTable(self, tableName, **columns):
        sql = "CREATE TABLE IF NOT EXISTS " + tableName + "( "
        for c,t in columns.items():
                sql += "%s %s, " % (c,t)
        sql = sql[:-2]+");"
        self.cursor.execute(sql)

    def addElement(self,tableName,**values):
        sql = "INSERT INTO " +tableName+" ("
        columns=[]
        value=[]
        for k,v in values.items():
                columns.append(k)
                value.append(v)
        for i in columns:
            sql+="%s, " % i
            sql = sql[:-2]+") VALUES ("
        for v in value:
                sql+="'%s', " % v
        sql=sql[:-2]+");"
        self.cursor.execute(sql)

    def viewTable(self, tableName):
        self.cursor.execute("SELECT * FROM %s" % tableName)
        print(self.cursor.fetchall())


newdb = Datab("second_with_python","localhost","root", "")
newdb.addTable("newTable", Id="int NOT NULL AUTO_INCREMENT PRIMARY KEY", First="varchar(40)", Last="varchar(40)")
newdb.addElement("newTable",First="David",Last="Backer")
# newdb.addElement("newTable",First="Jolita",Last="Kunciene")
newdb.viewTable("newTable")
