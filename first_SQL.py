import psycopg2

con = psycopg2.connect(database='testDB', user='postgres', password='skatastamoutra', host='localhost')

cur = con.cursor()

# cur.execute('ISERT INTO person (id Name Email Age);')

# cur.execute('INSERT INTO (Name) VALUES(%s)', ('Malakas'))

cur.execute("SELECT * FROM person;")

print(cur.fetchall())

