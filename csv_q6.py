import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

cur = con.cursor()

cur.execute("""
    select state, count(user_id) from python_db2.people group by state;
""")

rows = cur.fetchall()
for row in rows:
    print(row)