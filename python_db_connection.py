# Load the postgres module
import psycopg2
import csv

# Create a connection object
con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

# Create a cursor via the connection
cur = con.cursor()

with open('500-us-users.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute("""
            INSERT INTO python_db.users (first_name,
                last_name, address, city, county, state, zip, phone1, phone2)
                VALUES (%(f_name)s, %(l_name)s, %(address)s, %(city)s, %(county)s,
                    %(state)s, %(zip)s, %(phone1)s, %(phone2)s)
         """, {'f_name': row['first_name'],
                'l_name': row['last_name'],
                'address': row['address'],
                'city': row['city'],
                'county': row['county'],
                'state': row['state'],
                'zip': row['zip'],
                'phone1': row['phone1'],
                'phone2': row['phone2']
        })

con.commit()

# cur.execute("SET search_path TO python_db")
# cur.execute("select * from users")
# rows = cur.fetchall()
# for row in rows:
#    print(row)