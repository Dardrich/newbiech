'''Kalkulator Sederhana'''

def calc(a,b,operator):
    if operator == "+" :
      return a+b
    elif operator == "-":
      return a-b
    elif operator == "x":
      return a*b
    elif operator == "/":
      return a/b
    elif operator == "^":
      return a**b
    else:
      print("Masukkan operator yang benar")
      exit()
    

a = int(input("Masukkan bilangan bulat pertama: "))
operator = input("Masukkan operator aritmatika (+,-,x,/,^): ")
b = int(input("Masukkan bilangan bulat kedua: "))

print(f"Hasil {a} {operator} {b} adalah {calc(a,b,operator)}")
