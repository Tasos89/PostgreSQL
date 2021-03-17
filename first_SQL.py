import psycopg2
import psycopg2.extras

con = psycopg2.connect(database='testDB', user='postgres', password='skatastamoutra', host='localhost')

cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)

# cur.execute('INSERT INTO person (id Name Email Age) VALUES(%s)', (5,'Malakas','tooltasos#hotmail.com',33,))
# cur.execute('INSERT INTO person (Name)', ('Malakas',))


cur.execute("SELECT * FROM person WHERE id = %s;", (3,))

print('The person in table who has id = 2 is :', cur.fetchone()['Name'])

con.commit()

cur.close()

con.close()