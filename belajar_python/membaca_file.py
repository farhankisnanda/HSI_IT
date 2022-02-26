users = open("users.txt", "r")

array = users.readlines()
print(array)

index = 1
for item in array:
  print(f"{index} - {item}")
  index+= 1

users.close()