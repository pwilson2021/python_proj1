import psycopg2
import csv

# Create a connection object
con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

# Create a cursor via the connection
cur = con.cursor()
#
cur.execute(" create schema python_db2 " )

cur.execute("""
    create table python_db2.people(
            user_id  SERIAL PRIMARY KEY,
            state    char(2)   NULL,
            first_name  varchar(40) not null, last_name varchar(60) not null, address varchar(60) null,
            city varchar(60), county varchar(60), zip varchar(20) )
""")

cur.execute("""
    create table python_db2.phones(
                   id SERIAL PRIMARY KEY,
                   user_id  integer NULL REFERENCES python_db2.people(user_id),
                   phone1   varchar(20) NULL
                   )
""")

with open('500-us-users.csv', newline='') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        count += 1
        cur.execute("""
            INSERT INTO python_db2.people (first_name,
                last_name, address, city, county, state, zip)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
         """, (row['first_name'],
                row['last_name'],
                row['address'],
                row['city'],
                row['county'],
                row['state'],
                row['zip'],
        ))

        cur.execute(""" 
            INSERT INTO python_db2.phones(
                user_id, phone1
            ) VALUES (%s, %s)
        """, (count, row['phone1']))

        cur.execute(""" 
                    INSERT INTO python_db2.phones(
                        user_id, phone1
                    ) VALUES (%s, %s)
                """, (count, row['phone2']))

con.commit()