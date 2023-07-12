import random

random1 = random.randint(0,2)

def main():
  data = input("Pilih tipe suit Anda (gunting/batu/kertas): ").lower()

  if random1 == 0:
    print("Musuh mengeluarkan suit tipe: gunting")
    if data == "gunting":
      print("Anda mengeluarkan suit tipe:", data)
      print("Seri!")
    elif data == "batu":
      print("Anda mengeluarkan suit tipe:", data)
      print("Anda menang!")
    elif data == "kertas":
      print("Anda mengeluarkan suit tipe:", data)
      print("Maaf, Anda kalah")
    else:
      print("Masukkan yang benar!")
      main()
  if random1 == 1:
    print("Musuh mengeluarkan suit tipe: batu")
    if data == "batu":
      print("Anda mengeluarkan suit tipe:", data)
      print("Seri!")
    elif data == "kertas":
      print("Anda mengeluarkan suit tipe:", data)
      print("Anda menang!")
    elif data == "gunting":
      print("Anda mengeluarkan suit tipe:", data)
      print("Maaf, Anda kalah")
    else:
      print("Masukkan yang benar!")
      main()
  if random1 == 2:
    print("Musuh mengeluarkan suit tipe: kertas")
    if data == "kertas":
      print("Anda mengeluarkan suit tipe:", data)
      print("Seri!")
    elif data == "gunting":
      print("Anda mengeluarkan suit tipe:", data)
      print("Anda menang!")
    elif data == "batu":
      print("Anda mengeluarkan suit tipe:", data)
      print("Maaf, Anda kalah")
    else:
      print("Masukkan yang benar!")
      main()

def ask():
  restart = input("Ingin main lagi? (y/n): ").lower()

  if restart == "y":
     main()
     ask()
  elif restart == "n":
     exit()
  else:
     print("Please only enter y or n! ")
     ask()

main()
ask()
  