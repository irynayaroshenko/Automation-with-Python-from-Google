import csv


# f = open('csv_file.txt')
# csv_f = csv.reader(f)  # parse the file with csv module
# for row in csv_f:
#     name, phone, role = row
#     print(f'Name: {name:<15}Phone: {phone:<12}Role: {role}')
#
# f.close()

# write to csv-file
# There are two functions that we can use: writerow(), which we'll write one row at a time;
# and writerows(), which we'll write all of them together.
hosts = [['workstation.local', '192.168.25.46'], ['webserver.cloud', '10.2.5.6']]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

"""DictReader. This reader turns each row of the data in a CSV file into a dictionary. We can then access the data by using
the column names instead of the position in the row."""
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(f"{row['name']} has {row['users']} users.")

"""
We can use DictWriter in a similar way to generate a CSV file from the contents of a list of dictionaries.
This means that each element in the list will be a row in the file, and the values of each field will come out of each
of the dictionaries. For this to work, we'll also need to pass a list of the keys that we want to be stored
in the file when creating the writer. """
users = [
    {"name": "John Doe", "username": "johndoe", "department": "Engineering"},
    {"name": "Jane Smith", "username": "janesmith", "department": "Marketing"},
    {"name": "Mike Johnson", "username": "mikejohnson", "department": "Sales"}
]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()  # white first line (keys) in file
    writer.writerows(users)
