import pymysql

# prisijungimas prie host ir DB sukurimas
server = pymysql.connect(host="localhost", user="root", passwd="")
cursor = server.cursor()
sql = "CREATE DATABASE IF NOT EXISTS kursai_su_python;"
cursor.execute(sql)

# ieik i sukurta DB
sql = "USE kursai_su_python;"
cursor.execute(sql)

# sukurk joje lentele, jei dar tokia nesukurta
# trigubos kabutes, kad galetume rasyti koda per kelias eilutes
sql = '''CREATE TABLE IF NOT EXISTS owners(id integer NOT NULL AUTO_INCREMENT,
                                            name varchar(30) NOT NULL,
                                            gender varchar(7),
                                            phone varchar(10),
                                            PRIMARY KEY (id));'''
cursor.execute(sql)

# sukurk antra lentele, kuri bus susijusi su pirmaja
sql = '''CREATE TABLE IF NOT EXISTS pets(pet_id integer NOT NULL AUTO_INCREMENT,
                                            owner_id integer,
                                            name varchar(30) NOT NULL,
                                            gender varchar(7),
                                            species varchar(20),
                                            color varchar(10),
                                            age integer,
                                            PRIMARY KEY (pet_id),
                                            FOREIGN KEY (owner_id) REFERENCES owners(id));'''
cursor.execute(sql)

# patikrinti, paziureti visus duomenis
sql = "SHOW tables;"
cursor.execute(sql)
print(cursor.fetchall())
