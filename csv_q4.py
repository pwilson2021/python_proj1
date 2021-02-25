import csv
import numpy as np

with open('500-us-users.csv', newline='') as f, open('users.csv', 'w') as f2:
    reader = csv.DictReader(f)
    fieldnames = ['first_name', 'last_name', 'address', 'city','county', 'state', 'zip', 'phone1', 'phone2'  ]
    writer = csv.DictWriter(f2, fieldnames= fieldnames)
    for row in reader:
        # oneRow = np.array([[row['first_name'], row['last_name'], row['address'],
        #                     row['city'], row['county'], row['state'],
        #                     row['zip'], row['phone1'], row['phone2']
        #                     ]])
        # print(row)

        writer.writerow(rowdict=row)


