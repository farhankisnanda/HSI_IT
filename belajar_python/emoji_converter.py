kalimat = input(">>")

emoji_converter = {
  ":D": "😃",
  ":P": "🤪",
  ":C": "😠"
}

output = ""
kata = kalimat.split(" ")
for item in kata:
  output += emoji_converter.get(item, item) + " "

print(output)