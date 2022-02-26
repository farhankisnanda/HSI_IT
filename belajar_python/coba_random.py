import random

number = random.randint(1,5)

for item in range(5):
  number = random.randint(1,5)
  print(number)

users = ["Farhan","Rifda", "Muthia", "Kisnanda", "Muhammad" ]
for item in range(5):
  print(random.choice(users))