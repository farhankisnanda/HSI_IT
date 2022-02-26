kondisi = True

while kondisi:
  operator = input("Masukkan operator (+, -, /, *, exit)! ")
  if operator == "+" or operator == "-" or operator == "/" or operator == "*":
    angka1 = int(input("Masukkan angka pertama! "))
    angka2 = int(input("Masukkan angka kedua! "))
    if operator == "+":
      hasil = angka1 + angka2
      print(hasil)
    elif operator == "-":
      hasil = angka1 - angka2
      print(hasil)
    elif operator == "*": 
      hasil = angka1 * angka2
      print(hasil)
    elif operator == "/":
      hasil = angka1 // angka2
      print(hasil)
  elif operator == "exit":
    print("Terimakasih telah menggunakan kalkulator kami! ")
    break
  else:      
    print("Anda salah memasukkan operator")