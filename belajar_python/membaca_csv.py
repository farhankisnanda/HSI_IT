import csv
users = open("users.csv", "r")

users_csv = csv.reader(users, delimiter=",")
for item in users_csv:
  print(f"Nama: {item[0]}. Username: {item[1]}. Role: {item[2]}")
users.close()