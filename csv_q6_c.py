import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

cur = con.cursor()

cur.execute("""
    select p.first_name, p.zip from python_db2.people p join python_db2.people p2 on p.zip = p2.zip;"""
        )

rows = cur.fetchall()
for row in rows:
    print(row)