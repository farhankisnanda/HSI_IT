user = {
  "name": "M. Farhan Kisnanda",
  "age": 21,
  "is_admin": True
}

user["username"] = "farhankisnanda"
user["name"] = "M. Farhan K."

temp = user.get("name")
temp1 = user["username"]
temp2 = user.get("hobby", "Sepak bola")
temp3 = user.get("is_admin", False)
print(temp)
print(temp1)
print(temp2)
print(temp3)