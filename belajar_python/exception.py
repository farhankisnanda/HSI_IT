try:
  level = int(input("Level kamu: "))
  level = level/0
  print(level)
except ZeroDivisionError:
  print("Error tidak bisa dibagi 0")
except ValueError:
  print("Yang kamu masukkan bukan angka")

# untuk general bisa menggunakan except saja tanpa menyebutkan jenis errornya

# try:
#   ....
# except:
#   ....