import psycopg2

connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='Aingrifan',
    dbname='polban2'
)

cursor = connection.cursor()

cursor.execute("INSERT INTO mahasiswa (nim, nama, nomor_hp) VALUES (23456, 'Asep Mulyana', 8593030)")
connection.commit()
cursor.execute("SELECT nim, nama FROM mahasiswa")
data = cursor.fetchall()

for row in data:
    print(row)

#ISI KODE KITA

cursor.close()
connection.close()