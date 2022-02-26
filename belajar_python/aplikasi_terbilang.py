numbers = input("Masukkan angka: ")

numbers_mapping = {
  "1": "Satu",
  "2": "Dua",
  "3": "Tiga",
  "4": "Empat",
  "5": "Lima",
  "6": "Enam",
  "7": "Tujuh",
  "8": "Delapan",
  "9": "Sembilan"
}

output = ""
for item in numbers:
  terbilang = numbers_mapping.get(item, "Invalid")
  output += terbilang + " "

print(output)
