import csv

with open("users.csv", "r") as users:
  users_csv = csv.reader(users, delimiter=",")
  for item in users_csv:
    print(f"Nama: {item[0]}. Username: {item[1]}. Role: {item[2]}")

