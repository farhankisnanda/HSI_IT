kalimat = input(">>")

emoji_converter = {
  ":D": "ð",
  ":P": "ðĪŠ",
  ":C": "ð "
}

output = ""
kata = kalimat.split(" ")
for item in kata:
  output += emoji_converter.get(item, item) + " "

print(output)